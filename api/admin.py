from django.contrib import admin
from .models import Member, Payment, SingleVisit, Subscription, SubscriptionType

admin.site.site_header = "Formula Studio"
admin.site.site_title = "Formula Studio"

# Register your models here.

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mobile_number', 'email')
    search_fields = ('first_name', 'last_name')
    # list_filter = ('status', 'created', 'publish', 'author')
    # prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    # date_hierarchy = 'publish'
    ordering = ('last_name', 'first_name')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('member', 'payment_amount', 'payment_type', 'payment_paid', 'payment_date')
    list_filter = ('payment_type', 'payment_paid')

admin.site.register(SingleVisit)
admin.site.register(Subscription)
admin.site.register(SubscriptionType)
