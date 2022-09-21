from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.contrib.auth.models import User

from newsletter.models import NewsletterSubscriber


class Command(BaseCommand):
    help = "Reset bounce scores according to schedule"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for subscriber in NewsletterSubscriber.objects.all():
            if subscriber.reset_bounce_score_on >= datetime.utcnow():
                subscriber.bounce_score = 0
                if not subscriber.consent_withdrawn_at:
                    subscriber.subscribed = True
                subscriber.save()
