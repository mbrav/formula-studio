from django.contrib import admin
from .models import Member, Payment, Subscription, SubscriptionType

# Register your models here.

admin.site.register(Member)
admin.site.register(Payment)
admin.site.register(Subscription)
admin.site.register(SubscriptionType)
