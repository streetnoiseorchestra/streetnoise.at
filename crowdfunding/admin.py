from django.contrib import admin


from .models import Donation, Campaign


admin.site.register(Campaign)
admin.site.register(Donation)
