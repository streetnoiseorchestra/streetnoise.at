import re

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.contrib.auth.models import User

import requests
import dateutil
from dateutil.parser import parse as parse_date

import gigs
from home.models import HomePage2, FestivalPage
from gigs.models import GigPage, GigIndexPage

auth_url = "https://www.gig-o-matic.com/api/authenticate"
agenda_url = "https://www.gig-o-matic.com/api/agenda"


def authenticate(email, password):
    r = requests.post(auth_url, params={"email": email, "password": password})
    if r.status_code != 200:
        raise Exception("Gigo Login failed")
    return r.headers["set-cookie"]


def is_midnight(t):
    if t is None:
        return False
    return t.hour == 0 and t.minute == 0 and t.second == 0


def parse_time(val):
    if len(val.strip()) == 0:
        return None
    try:
        v = parse_date(val)
        if is_midnight(v):
            return None
        return v
    except dateutil.parser._parser.ParserError:
        return None


class Command(BaseCommand):
    help = "Sync all gigs from gigo to the website"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        if settings.GIGO_EMAIL is None or settings.GIGO_PASSWORD is None:
            raise Exception("Gigo user and pass not provided!")

        cookie = authenticate(settings.GIGO_EMAIL, settings.GIGO_PASSWORD)

        root_page = GigIndexPage.objects.live().first()
        if root_page is None:
            print("No Gig Index Page found. Aborting.")
            return

        r = requests.get(agenda_url, headers={"cookie": cookie})
        payload = r.json()
        if "upcoming_plans" not in payload:
            raise Exception("Failed to parse gigo response")

        for item in payload["upcoming_plans"]:
            band = item["band"]["shortname"]
            if band != settings.GIGO_BAND:
                continue
            gig = item["gig"]
            title = gig["title"]
            gig_id = gig["id"]

            if re.match("^Probe.*", title, re.I):
                print(f"skipping gig that is probably a probe: '{title}'")
                continue
            status = gig["status"]
            if status != 1:
                print(f"Ignoring unconfirmed gig '{title}'")
                continue
            is_in_trash = gig["is_in_trash"]
            if is_in_trash:
                print(f"Ignoring trashed gig '{title}'")
                continue
            location = parse_time(gig["address"])
            details = parse_time(gig["details"])
            calltime = parse_time(gig["calltime"])
            settime = parse_time(gig["settime"])
            endtime = parse_time(gig["endtime"])
            date_from = parse_date(gig["date"])
            if "enddate" in gig:
                date_to = parse_date(gig["enddate"])
            else:
                date_to = None
            try:
                # update existing gig page
                gig_page = GigPage.objects.get(gigomatic_id=gig_id).specific
                print(f"Updating gig '{title}'")
                gig_page.call_time = calltime
                gig_page.set_time = settime
                gig_page.end_time = endtime
                gig_page.date_from = date_from
                gig_page.date_to = date_to
                gig_page.location = location
                gig_page.body = details
                gig_page.save_revision(
                    submitted_for_moderation=True, user=User.objects.all().first()
                )

            except GigPage.DoesNotExist:
                # create new gig page
                print(f"Creating gig '{title}'")
                gig_page = GigPage(
                    gigomatic_id=gig_id,
                    date_from=date_from,
                    date_to=date_to,
                    set_time=settime,
                    call_time=calltime,
                    end_time=endtime,
                    title=title,
                    draft_title=title,
                    body=details,
                )
                gig_page.live = False
                root_page.add_child(instance=gig_page)
                gig_page.save_revision(
                    submitted_for_moderation=True, user=User.objects.all().first()
                )
