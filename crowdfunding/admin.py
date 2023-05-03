from django.contrib import admin


from .models import Donation, Campaign


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ("campaign_name", "goal", "start_dt", "end_dt", "creation_dt")


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = (
        "backer_name",
        "campaign_name",
        "amount_euros",
        "payment_id",
        "paid_dt",
    )
