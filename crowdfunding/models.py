from django.db import models
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)


class Campaign(models.Model):
    campaign_name = models.CharField(max_length=50, unique=True)
    goal = models.PositiveIntegerField()
    start_dt = models.DateTimeField(default=timezone.now)
    end_dt = models.DateTimeField()
    creation_dt = models.DateTimeField(default=timezone.now)


class Donation(models.Model):
    payment_id = models.CharField(max_length=255, unique=True)
    campaign = models.ForeignKey(
        Campaign, on_delete=models.CASCADE, related_name="donations"
    )
    backer_name = models.CharField(max_length=50)
    amount = models.PositiveIntegerField()
    payment_id = models.CharField(max_length=255)
    product_id = models.CharField(max_length=255)
    paid_dt = models.DateTimeField(default=timezone.now)

    class Meta:
        indexes = [
            models.Index(fields=["payment_id"]),
            models.Index(fields=["paid_dt"]),
        ]

    def __str__(self):
        return str(self.amount)

    @staticmethod
    def maybe_create_new(
        campaign_name, payment_id, product_id, backer_name, amount_total, creation_dt
    ):
        campaign = Campaign.objects.get(campaign_name=campaign_name)
        try:
            donation = Donation.objects.get(payment_id=payment_id)
            logger.info(
                f"skipping already seen payment donation id={donation.id} amount={donation.amount} payment_id={donation.payment_id}"
            )
            return None
        except Donation.DoesNotExist:
            donation = Donation(
                campaign=campaign,
                backer_name=backer_name,
                amount=amount_total,
                paid_dt=creation_dt,
                payment_id=payment_id,
                product_id=product_id,
            )
            donation.save()
            logger.info(
                f"created donation id={donation.id} amount={donation.amount} payment_id={donation.payment_id}"
            )
            return donation
