from django import forms
from django.db import models
from django.utils import timezone

# Create your models here.

class UserProfile(models.Model):
    first_name = models.CharField(
        ('First Name'),
        max_length=50,
    )

    last_name = models.CharField(
        ('Last Name'),
        max_length=50,
    )

    mobile_number = models.CharField(
        ('Mobile Number'),
        max_length=11,
        unique=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        ('Description'),
        blank=True,
    )

    created_at = models.DateField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    # image = models.ImageField(
    #     upload_to='img/member_profiles',
    #     blank=True,
    # )

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
        ordering = ('last_name','first_name')
        indexes = [
            models.Index(fields=['last_name', 'first_name']),
            models.Index(fields=['first_name'], name='first_name_idx'),
        ]

class Instructor(UserProfile):
    def revenue(self):
        money = 0
        # Count subs
        if self.subscriptions.all():
            for sub_v in self.subscriptions.all():
                if not sub_v.payment.writen_off:
                    money += sub_v.payment.amount
        # Count single visits
        if self.single_visits.all():
            for single_v in self.single_visits.all():
                if not single_v.payment.writen_off:
                    money += single_v.payment.amount
        # Count item purchases
        if self.item_purchases.all():
            for item_p in self.item_purchases.all():
                if not item_p.payment.writen_off:
                    money += item_p.payment.amount
        return money

    class Meta:
        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructors'
        ordering = ('last_name','first_name')

    def __str__(self):
        return "%s %s" % (self.last_name, self.first_name, )

class Member(UserProfile):
    # Count class visit stats for the member
    def visits_total(self):
        vis = 0
        if self.subscriptions.all():
            for sub in self.subscriptions.all():
                vis += sub.subscription_visits.all().count()
        if self.single_visits.all():
            vis += self.single_visits.all().count()
        return vis

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'
        ordering = ('last_name','first_name')

    def __str__(self):
        return "%s %s - #%s" % (self.last_name, self.first_name, self.id)

# A lose version for keep track of signups
# Best for integrating with an externa form field
# that submits new signups throguth an API call
class Signup(models.Model):
    date = models.DateTimeField(editable=False)

    # Best way to ass autosave
    # https://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.date = timezone.now()
        # self.modified = timezone.now()
        return super(Signup, self).save(*args, **kwargs)

    first_name = models.CharField(
        ('First Name'),
        max_length=50,
        blank=True,
    )

    last_name = models.CharField(
        ('Last Name'),
        max_length=50,
        blank=True,
    )

    mobile_number = models.CharField(
        ('Mobile Number'),
        max_length=11,
        blank=True,
    )

    email = models.EmailField(
        ('email'),
        blank=True,
    )

    group = models.CharField(
        ('Group'),
        max_length=50,
        blank=True,
    )

    member = models.ForeignKey('Member',
        on_delete = models.CASCADE,
        related_name='signups',
        help_text='Member to which to assign this signup',
        blank=True,
        null=True,
        # unique=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Signup'
        verbose_name_plural = 'Signups'
        # ordering = ('id')

class Payment(models.Model):
    PAYMENT_PAID = (
        ('0', 'Pending'),
        ('1', 'Paid'),
    )

    PAYMENT_TYPE = (
        ('0', 'Cash'),
        ('1', 'Transfer'),
        ('2', 'Card'),
    )

    date = models.DateField()

    writen_off = models.BooleanField(
        default=False,
        help_text="Set whether the payment should be written off from finances"
    )

    amount = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=10,
        blank=True,
    )

    method = models.CharField(
        max_length=2,
        choices=PAYMENT_TYPE,
        default="0",
    )

    status = models.CharField(
        max_length=2,
        choices=PAYMENT_PAID,
        default="1",
        help_text='Payment status',
    )

    member = models.ForeignKey('Member',
        on_delete = models.CASCADE,
        related_name='payments',
        help_text='Payments that member has made',
        # unique=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
        ordering = ('-date',)
        get_latest_by = 'date'

    def __str__(self):
        return "#%s – (%s)" % (self.id, self.date)

# TODO: ADD STAFF ENCASHMENT MODEL
# TODO: ADD ENCASHMENT MODEL

class GroupCategory(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(
        ('Description'),
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Group Category'
        verbose_name_plural = 'Group Categories'
        ordering = ('name',)

    def number_of_groups(self):
        return self.group.all().count()

    def __str__(self):
        return "%s" % (self.name)

class Group(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField()

    google_cal_id = models.CharField(
        max_length=30,
        default="",
        blank=True,
        null=True,
    )

    instructor = models.ForeignKey(
        'Instructor',
        related_name='groups',
        on_delete=models.CASCADE,
        help_text='Groups that the instructor leads',
    )

    category = models.ForeignKey(
        'GroupCategory',
        related_name='group',
        on_delete=models.CASCADE,
        help_text='Category of the group',
        # unique=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def revenue(self):
        # Get average price of subscription visit by dividing
        # its price by number of visits to get average
        money = 0
        for sub_v in self.subscription_visits.all():
            money += (sub_v.subscription.payment.amount /
                sub_v.subscription.subscription_category.number_of_visits)
        for single_v in self.single_visits.all():
            money += single_v.payment.amount
        return money

    def visits_total(self):
        vis = 0

        for sub_v in self.subscription_visits.all():
            vis += 1

        for single_v in self.single_visits.all():
            vis += 1
        return vis

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'
        ordering = ('-date',)

    def __str__(self):
        return "%s - %s" % (self.date.strftime("%b %d %Y"), self.name)

class SubscriptionCategory(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
    )

    description = models.TextField(
        ('Description'),
        blank=True,
    )

    price = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=10,
        blank=True,
    )

    number_of_visits = models.PositiveIntegerField(
        blank=False,
        null=False,
    )

    validity_in_days = models.PositiveIntegerField(
        blank=False,
        null=False,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def avg_visit_price(self):
        return int(self.price / self.number_of_visits)

    def total_count(self):
        return self.subscriptions.all().count()

    class Meta:
        verbose_name = 'Subscription Category'
        verbose_name_plural = 'Subscription Categories'
        ordering = ('price',)

    def __str__(self):
        return "%s" % (self.name)

class Subscription(models.Model):
    registration_date = models.DateField()

    def expiration_date(self):
        from datetime import datetime, timedelta
        days = self.subscription_category.validity_in_days
        if self.subscription_extensions.all():
            for ext in self.subscription_extensions.all():
                days += ext.days
        return self.registration_date + timedelta(days=days)

    def has_extension(self):
        if self.subscription_extensions.all():
            return True
        else:
            return False

    description = models.CharField(
        ('Description'),
        max_length=300,
        blank=True,
    )

    subscription_category = models.ForeignKey(
        'SubscriptionCategory',
        related_name='subscriptions',
        on_delete=models.CASCADE,
        # unique=True,
    )

    payment = models.ForeignKey(
        'Payment',
        related_name='subscription',
        on_delete=models.CASCADE,
        # unique=True,
    )

    member = models.ForeignKey('Member',
        on_delete = models.CASCADE,
        related_name='subscriptions',
        help_text='Subscriptions that the member has',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def visits_total(self):
        return self.subscription_category.number_of_visits

    def visits_made(self):
        return self.subscription_visits.all().count()

    def visits_remaining(self):
        return (
            self.subscription_category.number_of_visits -
            self.subscription_visits.all().count()
        )

    class Meta:
         verbose_name = 'Subscription'
         verbose_name_plural = 'Subscriptions'
         ordering = ('-registration_date',)

    def __str__(self):
        return "%s – (%s)" % (self.member, self.registration_date)

class SubscriptionExtension(models.Model):
    date = models.DateField()

    days = models.PositiveIntegerField(
        blank=False,
        null=False,
    )

    description = models.TextField(
        ('Description'),
        blank=True,
    )

    subscription = models.ForeignKey(
        'Subscription',
        related_name='subscription_extensions',
        on_delete=models.CASCADE,
        # unique=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
         verbose_name = 'Subscription Extension'
         verbose_name_plural = 'Subscription Extensions'
         ordering = ('-date',)

    def __str__(self):
        return "%s – (%s)" % (self.id, self.date)

class SubscriptionVisit(models.Model):

    group = models.ForeignKey(
        'Group',
        related_name='subscription_visits',
        on_delete=models.CASCADE,
        # unique=True,
    )

    subscription = models.ForeignKey('Subscription',
        on_delete=models.CASCADE,
        blank=False,
        related_name='subscription_visits',
        help_text='A visit based on a subscription',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Subscription Visit'
        verbose_name_plural = 'subscription Visits'
        ordering = ('-group__date',)

    def date(self):
        return self.group.date

    def __str__(self):
        return "%s" % (self.group)

class SingleVisit(models.Model):
    payment = models.ForeignKey(
        'Payment',
        related_name='single_visit',
        on_delete=models.CASCADE,
        help_text='Group to which a single visit occured',
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    group = models.ForeignKey(
        'Group',
        related_name='single_visits',
        on_delete=models.CASCADE,
        help_text='Single visits that the group has',
        # unique=True,
    )

    member = models.ForeignKey('Member',
        on_delete = models.CASCADE,
        related_name='single_visits',
        help_text='Single visits that the member has made',
        # unique=True,
    )

    def date(self):
        return self.group.date

    class Meta:
        verbose_name = 'Single Visit'
        verbose_name_plural = 'Single Visits'
        ordering = ('-group__date',)

    def __str__(self):
        return "%s" % (self.payment)

class ItemCategory(models.Model):
    name = models.CharField(max_length=30)

    price = models.DecimalField(
        default=0,
        decimal_places=2,
        max_digits=10,
        blank=True,
    )

    description = models.TextField(
        ('Description'),
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Item Category'
        verbose_name_plural = 'Item Categories'
        ordering = ('price',)

    def __str__(self):
        return "%s" % (self.name)

class ItemPurchase(models.Model):
    def date(self):
        return self.payment.date

    item_category = models.ForeignKey(
        'ItemCategory',
        related_name='items',
        on_delete=models.CASCADE,
        # unique=True,
    )

    payment = models.ForeignKey(
        'Payment',
        related_name='item_purchases',
        on_delete=models.CASCADE,
        # unique=True,
    )

    member = models.ForeignKey('Member',
        on_delete = models.CASCADE,
        related_name='item_purchases',
        help_text='Item purchases that the member has made',
        # unique=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Item Purchase'
        verbose_name_plural = 'Item Purchases'

    def __str__(self):
        return "%s" % (self.item_category)
