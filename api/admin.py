from django.contrib import admin
from .models import Member, Payment, GroupCategory, Group, SubscriptionCategory, Subscription, SubscriptionVisit, SingleVisit, ItemPurchase

admin.site.site_header = "Formula Studio"
admin.site.site_title = "Formula Studio"

# Register your models here.

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name',  'mobile_number', 'email')
    search_fields = ('last_name', 'first_name')
    # list_filter = ('status', 'created', 'publish', 'author')
    # prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    # date_hierarchy = 'publish'
    ordering = ('last_name', 'first_name')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('member', 'payment_amount', 'payment_type', 'payment_paid', 'payment_date')
    list_filter = ('payment_type', 'payment_paid')
    list_editable = ['payment_type', 'payment_paid']

admin.site.register(GroupCategory)
admin.site.register(Group)

@admin.register(SubscriptionCategory)
class SubscriptionCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_visits', 'validity_in_days', 'price')
    ordering = ('price', 'name')

admin.site.register(Subscription)
admin.site.register(SubscriptionVisit)
admin.site.register(SingleVisit)
admin.site.register(ItemPurchase)
