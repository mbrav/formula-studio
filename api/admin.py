from django.contrib import admin
from .models import Member, Payment, GroupCategory, Group, SubscriptionCategory, Subscription, SubscriptionVisit, SingleVisit, ItemCategory, ItemPurchase

admin.site.site_header = "Formula Studio"
admin.site.site_title = "Formula Studio"
admin.site.index_title = "The best CMS ever written!"

# Register your models here.

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'last_name', 
        'first_name', 
        'mobile_number', 
        'email'
    )

    search_fields = (
        'last_name', 
        'first_name'
    )

    # list_filter = ('status', 'created', 'publish', 'author')
    # prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    # date_hierarchy = 'publish'

    ordering = (
        'last_name', 
        'first_name'
    )

#Inline elements 

# class SingleVisitInline(admin.StackedInline):
class SingleVisitInline(admin.TabularInline):
    model = SingleVisit
    max_num=1

class SubscriptionInline(admin.TabularInline):
    model = Subscription
    max_num=1
    
class ItemPurchaseInline(admin.TabularInline):
    model = ItemPurchase
    max_num=3

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_filter = ("member", "paid", "writen_off",)
    list_display = (
        'member', 
        'amount', 
        'method', 
        'paid', 
        'date',
        'writen_off',
    )

    list_filter = (
        'method', 
        'paid',
    )

    list_editable = [
        'method', 
        'paid',
        'writen_off',
    ]

    inlines = [
        SingleVisitInline,
        SubscriptionInline,
        ItemPurchaseInline,
    ]

admin.site.register(GroupCategory)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'category', 
        'visits_total', 
        'revenue_amount', 
        'date', 
    )

    ordering = (
        '-date', 
    )

@admin.register(SubscriptionCategory)
class SubscriptionCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'number_of_visits', 
        'validity_in_days', 
        'avg_visit_price',
        'price',
    )

    ordering = (
        'price', 
        'name'
    )

admin.site.register(Subscription)
admin.site.register(SubscriptionVisit)

@admin.register(SingleVisit)
class SingleVisitAdmin(admin.ModelAdmin):
    list_display = (
        'date', 
        'member',
        'group',
    )

    ordering = (
        'date',
        'group',
    )


@admin.register(ItemCategory)
class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'price',
    )

    ordering = (
        'price', 
        'name',
    )

admin.site.register(ItemPurchase)
