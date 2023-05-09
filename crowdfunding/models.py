from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.timesince import timesince
from django.utils.translation import get_language
from django.contrib.humanize.templatetags.humanize import (
    intcomma,
    naturaltime,
    naturalday,
)

from datetime import timedelta
import logging


logger = logging.getLogger(__name__)


class Campaign(models.Model):
    campaign_name = models.CharField(max_length=50, unique=True)
    goal = models.PositiveIntegerField()
    stretch_goal1 = models.PositiveIntegerField(null=True)
    stretch_goal2 = models.PositiveIntegerField(null=True)
    start_dt = models.DateTimeField(default=timezone.now)
    end_dt = models.DateTimeField()
    creation_dt = models.DateTimeField(default=timezone.now)

    @cached_property
    def all_donations(self):
        return self.donations.all()

    @cached_property
    def is_live(self):
        return self.has_started and not self.has_ended

    @cached_property
    def has_started(self):
        return timezone.now() >= self.start_dt

    @cached_property
    def has_ended(self):
        return timezone.now() >= self.end_dt

    @cached_property
    def days_remaining(self):
        return (self.end_dt - timezone.now()).days

    @cached_property
    def total_backers(self):
        return len(self.all_donations)

    @cached_property
    def total_raised(self):
        return sum([d.amount / 100 for d in self.all_donations if d.amount > 0])

    @cached_property
    def raised_percent(self):
        total_raised = self.total_raised
        goals = [
            goal for goal in [self.goal, self.stretch_goal1, self.stretch_goal2] if goal
        ]
        goal = goals[0]
        return round(total_raised / goal * 100, 0)

    @cached_property
    def raised_percent_css(self):
        total_raised = self.total_raised
        goal = self.goal
        return "{:.9f}".format(total_raised / goal * 100)

    @cached_property
    def raised_percent_css_final(self):
        total_raised = self.total_raised
        goal = self.final_goal
        return "{:.9f}".format(total_raised / goal * 100)

    @cached_property
    def raised_percent_css_stretch_goal1(self):
        total_raised = self.total_raised
        goal = self.stretch_goal1
        return "calc({:.9f}% + 0.5em);".format(total_raised / goal * 100)

    @cached_property
    def raised_percent_css_stretch_goal2(self):
        total_raised = self.total_raised
        goal = self.stretch_goal2
        return "calc({:.9f}% + 0.5em);".format(total_raised / goal * 100)

    @cached_property
    def backers(self):
        b = []
        for backer in self.all_donations:
            if backer.amount > 0:
                b.append(backer)
        return b

    @cached_property
    def is_successful(self):
        if self.stretch_goal2:
            return self.total_raised >= self.stretch_goal2
        elif not self.stretch_goal2 and self.stretch_goal1:
            return self.total_raised >= self.stretch_goal1
        else:
            return self.total_raised >= self.goal

    @cached_property
    def should_show_supporter_names(self):
        return self.total_backers >= 3

    @cached_property
    def goal_reached(self):
        return self.total_raised >= self.goal

    @cached_property
    def stretch_goal1_reached(self):
        if self.stretch_goal1:
            return self.total_raised >= self.stretch_goal1
        return False

    @cached_property
    def stretch_goal2_reached(self):
        if self.stretch_goal2:
            return self.total_raised >= self.stretch_goal2
        return False

    @cached_property
    def in_stretch(self):
        if self.goal_reached and (self.stretch_goal1 or self.stretch_goal2):
            return True
        return False

    @cached_property
    def next_level_goal(self):
        for goal in [self.goal, self.stretch_goal1, self.stretch_goal2]:
            if goal > self.total_raised:
                return goal
        return self.goal

    @cached_property
    def final_goal(self):
        goals = [self.goal, self.stretch_goal1, self.stretch_goal2]
        for goal in goals:
            if self.total_raised > goal:
                continue
            return goal
        return max(goals)


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

    @property
    def paid_at(self):
        now = timezone.now()
        date = self.paid_dt
        # date = now - timedelta(days=7)
        delta = now - date
        lang = get_language()
        if delta >= timedelta(days=1):
            if lang == "de":
                if delta.days > 1:
                    return f"vor {delta.days} Tagen"
                else:
                    return f"ein Tag her"
            else:
                if delta.days > 1:
                    return f"{delta.days} days ago"
                else:
                    return f"one day ago"
        else:
            return naturaltime(date)

    @property
    def campaign_name(self):
        return self.campaign.campaign_name

    @property
    def amount_euros(self):
        if self.amount and self.amount > 0:
            return round(self.amount / 100, 2)
        return self.amount

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
