from django.contrib import admin
from .models import Instructor, Member, Payment, GroupCategory, Group, SubscriptionCategory, Subscription, SubscriptionVisit, SingleVisit, ItemCategory, ItemPurchase

admin.site.site_header = "Formula Studio"
admin.site.site_title = "Formula Studio"
admin.site.index_title = "The best CMS ever written!"

# For filtering admin dropdown menu 
# https://books.agiliq.com/projects/django-admin-cookbook/en/latest/filter_fk_dropdown.html

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

# Register your models here.

@admin.register(Instructor)
class Instructor(admin.ModelAdmin):
    list_per_page = 200
    list_display = (
        'last_name', 
        'first_name', 
        'mobile_number', 
        'email',
    )

    search_fields = (
        'last_name', 
        'first_name'
    )

    ordering = (
        'last_name', 
        'first_name'
    )

    # readonly_fields = ['revenue_amount','visits_total']

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_per_page = 200
    list_display = (
        'last_name', 
        'first_name', 
        'mobile_number', 
        'email',
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

    readonly_fields = ['revenue_amount','visits_total']
    
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_filter = ("member", "paid", "writen_off",)
    date_hierarchy = 'date'
    list_per_page = 200
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

    raw_id_fields = ['member']
    
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

    readonly_fields = ['visits_total']

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

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_per_page = 200
    date_hierarchy = 'registration_date'
    list_display = (
        'member',
        'registration_date', 
        'visits_made',
        'visits_remaining',
        'visits_total',
    )

    ordering = (
        'registration_date',
    )

    readonly_fields = ['visits_made', 'visits_remaining', 'visits_total',]

@admin.register(SubscriptionVisit)
class SubscriptionVisitAdmin(admin.ModelAdmin):
    list_per_page = 200
    date_hierarchy = 'date'
    list_display = (
        'subscription',
        'date', 
    )

    ordering = (
        'date',
    )

@admin.register(SingleVisit)
class SingleVisitAdmin(admin.ModelAdmin):
    list_per_page = 200
    date_hierarchy = 'date'
    list_display = (
        'date', 
        'member',
        'group',
    )

    ordering = (
        'date',
        'group',
    )

    raw_id_fields = ['member']

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
