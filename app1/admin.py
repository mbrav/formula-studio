from django.contrib import admin
from .models import Member, Payment, SingleVisit, Subscription, SubscriptionType

# Register your models here.

admin.site.register(Member)
admin.site.register(Payment)
admin.site.register(SingleVisit)
admin.site.register(Subscription)
admin.site.register(SubscriptionType)
