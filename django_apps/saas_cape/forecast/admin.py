from django.contrib import admin

from .models import Forecast, Subscription

admin.site.register(Forecast)
admin.site.register(Subscription)
