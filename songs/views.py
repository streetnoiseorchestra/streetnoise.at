import json
import logging
import uuid

import dateutil.parser
from django.conf import settings
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import SongIndexPage, SongPage

logger = logging.getLogger(__name__)


def song_page_update(payload) -> bool:
    """Returns true when a page is created, false when not"""

    snorga_id = uuid.UUID(payload["snorga_id"])
    title = payload["title"]
    status = payload["status"]
    arrangement_credits = payload.get("arrangement_credits")
    composition_credits = payload.get("composition_credits")
    lyrics = payload.get("lyrics")
    last_played_date = payload.get("last_played_date")
    description = payload.get("description")
    arrangement_notes = payload.get("arrangement_notes")

    if last_played_date:
        last_played_date = dateutil.parser.isoparse(last_played_date)

    should_publish = description and len(description) > 20
    try:
        song_page = SongPage.objects.get(snorga_id=snorga_id).specific
        song_page.title = title
        song_page.arrangement_credits = arrangement_credits
        song_page.composition_credits = composition_credits
        song_page.arrangement_notes = arrangement_notes
        song_page.status = status
        song_page.lyrics = lyrics
        song_page.last_played_date = last_played_date
        song_page.description = description
        revision = song_page.save_revision(user=User.objects.all().first())
        if should_publish:
            revision.publish()
        return False
    except SongPage.DoesNotExist:
        song_page = SongPage(
            snorga_id=snorga_id,
            title=title,
            draft_title=title,
            status=status,
            arrangement_credits=arrangement_credits,
            composition_credits=composition_credits,
            arrangement_notes=arrangement_notes,
            lyrics=lyrics,
            last_played_date=last_played_date,
            description=description,
        )
        if should_publish:
            song_page.live = True
        else:
            # probably needs more work
            song_page.live = False
        root_page = SongIndexPage.objects.live().first()
        root_page.add_child(instance=song_page)
        revision = song_page.save_revision(user=User.objects.all().first())
        if should_publish:
            revision.publish()
        return True


@csrf_exempt
@require_POST
def song_update_handler(request):
    token = settings.SNORGA_SHARED_TOKEN
    if request.headers.get("Authorization", "") != f"Bearer {token}":
        return JsonResponse({"error": "Unauthorized"}, status=401)

    try:
        data = json.loads(request.body)
    except ValueError:
        logger.error("invalid JSON posted to /api/song/", exc_info=True)
        return JsonResponse({"error": "invalid json"}, status=400)
    try:
        snorga_id = data.get("snorga_id")
        if not snorga_id:
            return JsonResponse({"error": "snorga_id is required"}, status=400)
        try:
            uuid.UUID(snorga_id)
        except ValueError:
            return JsonResponse({"error": "invalid snorga_id"}, status=400)
        title = data.get("title", "")
        if len(title) == 0:
            return JsonResponse({"error": "title must be non-empty"}, status=400)
        status = data.get("status")
        if status and status not in SongPage.Status.values:
            return JsonResponse({"error": "invalid status"}, status=400)

        created = song_page_update(data)
        return JsonResponse({"snorga_id": snorga_id, "created": created}, status=201 if created else 200)
    except Exception:
        logger.error("failed to update song", exc_info=True)
        return JsonResponse({"error": "something went wrong"}, status=500)
