from django.contrib import admin
from .models import Instructor, Member, Signup, Payment, GroupCategory, Group, SubscriptionCategory, Subscription, SubscriptionExtension, SubscriptionVisit, SingleVisit, ItemCategory, ItemPurchase

admin.site.site_header = "Formula Studio"
admin.site.site_title = "Formula Studio"
admin.site.index_title = "The best CMS ever written!"

# For filtering admin dropdown menu
# https://books.agiliq.com/projects/django-admin-cookbook/en/latest/filter_fk_dropdown.html

# Inline elements
# class MemberInline(admin.StackedInline):
#     model = Member
#     max_num=1


class SingleVisitInline(admin.TabularInline):
    model = SingleVisit
    max_num = 1


class SubscriptionInline(admin.TabularInline):
    model = Subscription
    max_num = 1


class ItemPurchaseInline(admin.TabularInline):
    model = ItemPurchase
    max_num = 3


# Register your models here.

@admin.register(Instructor)
class Instructor(admin.ModelAdmin):
    list_per_page = 100
    list_display = (
        'last_name',
        'first_name',
        'mobile_number',
        'email',
        'id'
    )

    search_fields = (
        'last_name',
        'first_name'
    )

    ordering = (
        'last_name',
        'first_name'
    )


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_per_page = 100
    list_display = (
        'last_name',
        'first_name',
        'mobile_number',
        'email',
        'id'
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
        'first_name',
    )


@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    list_per_page = 100
    list_display = (
        'created_at',
        'last_name',
        'first_name',
        'group',
        'single_visit',
        'subscription_visit',
        'id'
    )

    search_fields = (
        'last_name',
        'first_name',
        'group',
    )

    list_editable = [
        'single_visit',
        'subscription_visit'
    ]

    # list_filter = ('status', 'created', 'publish', 'author')
    # prepopulated_fields = {'slug': ('title',)}
    # raw_id_fields = ('author',)
    # date_hierarchy = 'publish'

    ordering = (
        '-created_at',
    )

    readonly_fields = ['last_name', 'first_name',
                       'mobile_number', 'email', 'group_google_cal_id']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_filter = ("member", "status", "writen_off",)
    date_hierarchy = 'date'
    list_per_page = 100
    list_display = (
        'member',
        'amount',
        'method',
        'status',
        'date',
        'writen_off',
        'id',
    )

    list_filter = (
        'method',
        'status',
    )

    list_editable = [
        'status',
        'writen_off',
    ]

    ordering = (
        '-date',
    )

    inlines = [
        SingleVisitInline,
        SubscriptionInline,
        ItemPurchaseInline,
    ]


@admin.register(GroupCategory)
class GroupCategoryAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = (
        'name',
        'number_of_groups',
        'id',
    )

    search_fields = (
        'name',
    )

    ordering = (
        'name',
    )

    readonly_fields = ['number_of_groups']


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = (
        'date',
        'name',
        'category',
        'instructor',
        'id',
    )

    list_editable = [
        'category',
        'instructor',
    ]

    search_fields = (
        'name',
        'category',
        'instructor',
    )

    list_filter = (
        'instructor',
        'category',
    )

    ordering = (
        '-date',
    )

    readonly_fields = ['google_cal_id']


@admin.register(SubscriptionCategory)
class SubscriptionCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'number_of_visits',
        'validity_in_days',
        'avg_visit_price',
        'price',
        'id',
    )

    ordering = (
        'price',
        'name',
    )


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_per_page = 50
    date_hierarchy = 'registration_date'
    list_display = (
        'member',
        'registration_date',
        'has_extension',
        'id',
    )

    ordering = (
        '-id',
        'registration_date',
    )

    readonly_fields = [
        'expiration_date'
    ]

    readonly_fields = ['has_extension']


@admin.register(SubscriptionExtension)
class SubscriptionExtensionAdmin(admin.ModelAdmin):
    list_per_page = 50
    # date_hierarchy = 'date'
    list_display = (
        'date',
        'subscription',
        'days',
        'id',
    )

    ordering = (
        '-id',
        'date',
    )


@admin.register(SubscriptionVisit)
class SubscriptionVisitAdmin(admin.ModelAdmin):
    list_per_page = 100
    list_display = (
        'subscription',
        'id',
    )

    ordering = (
        '-id',
        'group',
    )


@admin.register(SingleVisit)
class SingleVisitAdmin(admin.ModelAdmin):
    list_per_page = 100
    list_display = (
        'member',
        'group',
        'id',
    )

    ordering = (
        '-id',
        'group',
    )

    search_fields = (
        'group',
    )

    list_editable = [
        'group',
    ]


@admin.register(ItemCategory)
class ItemCategoryAdmin(admin.ModelAdmin):
    list_per_page = 100

    list_display = (
        'name',
        'price',
        'id',
    )

    ordering = (
        'price',
        'name',
    )


@admin.register(ItemPurchase)
class ItemPurchaseAdmin(admin.ModelAdmin):
    list_per_page = 100
    list_display = (
        'item_category',
        'id',
    )

    ordering = (
        '-id',
        'item_category',
    )
