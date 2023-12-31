import datetime
import json
import logging
import pprint

import stripe
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from stripe.error import SignatureVerificationError

from .models import Campaign, Donation

logger = logging.getLogger(__name__)

pp = pprint.PrettyPrinter(indent=2)


@method_decorator(csrf_exempt, name="dispatch")
def stripe_webhooks(request):
    stripe.api_key = settings.STRIPE_SK
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    try:
        sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
        event = stripe.Webhook.construct_event(request.body, sig_header, endpoint_secret)

    except ValueError as e:
        print("Webhook error while parsing request payload" + str(e))
        return JsonResponse({"success": False}, status=400)
    except SignatureVerificationError as e:
        print("Webhook error while verifying Stripe signature" + str(e))
        return JsonResponse({"success": False}, status=400)

    event_dict = event.to_dict()
    logger.info(f"processing webhook id={event_dict['id']} type={event_dict['type']}")

    if event_dict["type"] == "checkout.session.completed":
        checkout_session = event_dict["data"]["object"]
        handle_checkout_session_succeeded(checkout_session)
    return JsonResponse({"success": True}, status=200)


def get_campaign_from_line_item(line_item):
    price = line_item.get("price")
    if price:
        product = stripe.Product.retrieve(price["product"])
        md = product.get("metadata")
        if md:
            return md.get("campaign_name")


def handle_checkout_session_succeeded(checkout_session):
    if checkout_session["object"] != "checkout.session":
        logger.error(
            f"handle_checkout_session_succeeded: received stripe webhook we can't handle object={checkout_session['object']} id={checkout_session['id']}"
        )
    payment_intent = checkout_session["payment_intent"]
    backer_name = None
    for field in checkout_session["custom_fields"]:
        if field["key"] in [
            "nametoappearinourpubliclistofbackers",
            "nameerscheintinderffentlichenspenderliste",
        ]:
            backer_name = field["text"].get("value")
    if backer_name:
        backer_name = backer_name.strip()
    if not backer_name or len(backer_name) <= 1:
        backer_name = "Anonym"
    amount_total = checkout_session["amount_total"]
    creation_dt = datetime.datetime.fromtimestamp(checkout_session["created"])
    campaign_name = None
    product_id = None

    if checkout_session["id"].startswith("cs_test_") and checkout_session["payment_link"] in [
        "plink_1N3ikhGN3fhIGpkEAzmGxNAH"
    ]:
        campaign_name = "test-campaign"
        product_id = "no-reward"
    elif checkout_session["id"].startswith("cs_") and checkout_session["payment_link"] in [
        "plink_1N5sb7GN3fhIGpkEMcekm38Y"
    ]:
        campaign_name = "crowdfunding-2023"
        product_id = "no-reward"
    else:
        expanded_session = stripe.checkout.Session.retrieve(checkout_session["id"], expand=["line_items"]).to_dict()
        for line_item in expanded_session["line_items"]["data"]:
            campaign_name = get_campaign_from_line_item(line_item)
            if campaign_name:
                product_id = line_item["price"]["product"]
                break

    if not campaign_name:
        logger.error(
            f"handle_checkout_session_: failed. received stripe webhook we can't handle id={checkout_session['id']} no campaign name found"
        )
        return False

    donation = Donation.maybe_create_new(
        campaign_name,
        payment_intent,
        product_id,
        backer_name,
        amount_total,
        creation_dt,
    )

    return True
