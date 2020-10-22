from django.contrib import admin
from .models import Member, Subscription, SubscriptionType
# Register your models here.

admin.site.register(Member)
admin.site.register(Subscription)
admin.site.register(SubscriptionType)
