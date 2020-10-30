from django import forms
from django.db import models
# from django.conf import settings

# Create your models here.

class UserProfile(models.Model):
    first_name = models.CharField(
        ('First Name'), 
        max_length=50
    )

    last_name = models.CharField(
        ('Last Name'), 
        max_length=50
    )

    mobile_number = models.CharField(
        ('Mobile Number'), 
        max_length=11, 
        # unique=True, 
        # blank=false,
        unique=False, 
        blank=True,
    )

    email = models.EmailField(
        null=True, 
        blank=True, 
        unique=True
    )

    description = models.TextField(
        ('Description'), 
        blank=True
    )

    registered_on = models.DateField(
        auto_now_add=True
    )

    image = models.ImageField(
        upload_to='img/member_profiles', 
        blank=True
    )

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
        ordering = ('last_name','first_name')
        indexes = [
            models.Index(fields=['last_name', 'first_name']),
            models.Index(fields=['first_name'], name='first_name_idx'),
        ]

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Instructor(UserProfile):

    def revenue_amount(self):
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

class Member(UserProfile):

    # Count revenue stats for the member
    def revenue_amount(self):
        money = 0
        if self.groups.all():
            # Count subs
            for group in self.groups.all():
                for visit in group.subscription_visits.all():
                    if not visit.subscription.payment.writen_off:
                        money += visit.subscription.payment.amount
            # Count single visits 
            if self.groups.single_visits.all():
                for single_v in self.groups.single_visits.all():
                    if not single_v.payment.writen_off:
                        money += single_v.payment.amount   
        return money

    # Count class visit stats for the member
    def visits_total(self):
        return self.subscription_visits.all().count() + self.single_visits.all().count()

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

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
        blank=True
    )

    method = models.CharField(
        max_length=2,
        choices=PAYMENT_TYPE,
        default="0" 
    )

    paid = models.CharField(
        max_length=2,
        choices=PAYMENT_PAID,
        default="1"
    )

    member = models.ForeignKey('Member', 
        on_delete = models.CASCADE,
        related_name='payments',
        help_text='Payments that member has made',
        # unique=True,
    )

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
        blank=True
    )

    class Meta:
        verbose_name = 'Group Category'
        verbose_name_plural = 'Group Categories'

    def __str__(self):
        return "%s" % (self.name)

class Group(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField()

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
    
    def revenue_amount(self):
        money = 0
        
        # Get average price of subscription visit by dividing
        # its price by number of visits to get average 
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

    # TODO: ADD INSTRUCTOR / USER (?) MODEL

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

    def __str__(self):
        return "%s" % (self.name)
    
class SubscriptionCategory(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True, 
    )

    description = models.TextField(
        ('Description'), 
        blank=True
    )

    price = models.DecimalField(
        default=0, 
        decimal_places=2, 
        max_digits=10, 
        blank=True
    )

    number_of_visits = models.PositiveIntegerField(
        blank=False, 
        null=False
    )

    validity_in_days = models.PositiveIntegerField(
        blank=False, 
        null=False
    )

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

# TODO: ADD SUBSCRIPTION EXTENSION MODEL

class Subscription(models.Model):
    registration_date = models.DateField()
    description = models.CharField(
        ('Description'),
        max_length=300,
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
        help_text='Subscriptions that the member has'
    )

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

class SubscriptionVisit(models.Model):
    date = models.DateField()
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
        help_text='A visit based on a subscription'
    )

    class Meta:
        verbose_name = 'Subscription Visit'
        verbose_name_plural = 'subscription Visits'
        ordering = ('-date',)

    def __str__(self):
        return "%s" % (self.group)

class SingleVisit(models.Model):
    date = models.DateField()
    payment = models.ForeignKey(
        'Payment', 
        related_name='single_visit', 
        on_delete=models.CASCADE,
        help_text='Group to which a single visit occured',
    )

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

    class Meta:
        verbose_name = 'Single Visit'
        verbose_name_plural = 'Single Visits'
        ordering = ('-date',)

    def __str__(self):
        return "%s" % (self.payment)

class ItemCategory(models.Model):
    name = models.CharField(max_length=30)

    price = models.DecimalField(
        default=0, 
        decimal_places=2, 
        max_digits=10, 
        blank=True
    )

    description = models.TextField(
        ('Description'), 
        blank=True
    )

    class Meta:
        verbose_name = 'Item Category'
        verbose_name_plural = 'Item Categories'
        ordering = ('price',)

    def __str__(self):
        return "%s" % (self.name)

class ItemPurchase(models.Model):
    date = models.DateField()
    
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

    class Meta:
        verbose_name = 'Item Purchase'
        verbose_name_plural = 'Item Purchases'

    def __str__(self):
        return "%s – (%s)" % (self.item_category, self.date)





