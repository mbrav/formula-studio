from django.db import models
from django import forms

# Create your models here.

class Member(models.Model):
    first_name = models.CharField(('First Name'), max_length=50)
    last_name = models.CharField(('Last Name'), max_length=50)
    mobile_number = models.CharField(('Mobile Number'), max_length=11, unique=True, blank=False)
    email = models.EmailField(null=True, blank=True, unique=True)
    description = models.CharField(('Description'), max_length=300, blank=True)
    registered_on = models.DateField(auto_now_add=True)

    image = models.ImageField(upload_to='img/member_profiles', blank=True)

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

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

    payment_date = models.DateField()

    payment_amount = models.DecimalField(
        default=0, 
        decimal_places=2, 
        max_digits=10, 
        blank=True
    )

    payment_type = models.CharField(
        max_length=2,
        choices=PAYMENT_TYPE, 
    )

    payment_paid = models.CharField(
        max_length=2,
        choices=PAYMENT_PAID, 
    )

    member = models.ForeignKey('Member', 
        on_delete = models.CASCADE,
        related_name='payments',
        help_text='Payments that member has made'
    )

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
        ordering = ('-payment_date',)

    def __str__(self):
        return "#%s – (%s)" % (self.id, self.payment_date)

# TODO: ADD ENCASHMENT MODEL

class GroupCategory(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(('Description'), max_length=300, blank=True)

    class Meta:
        verbose_name = 'Group Category'
        verbose_name_plural = 'Group Categories'

    def __str__(self):
        return "%s" % (self.name)

class Group(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField()
    category = models.ForeignKey('GroupCategory', related_name='group', on_delete=models.CASCADE)

    # TODO: ADD INSTRUCTOR / USER (?) MODEL

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

    def __str__(self):
        return "%s" % (self.name)
    
class SubscriptionCategory(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(('Description'), max_length=300, blank=True)
    price = models.DecimalField(
        default=0, 
        decimal_places=2, 
        max_digits=10, 
        blank=True
    )
    number_of_visits = models.PositiveIntegerField(blank=False, null=False)
    validity_in_days = models.PositiveIntegerField(blank=False, null=False)

    class Meta:
        verbose_name = 'Subscription Category'
        verbose_name_plural = 'Subscription Categories'

    def __str__(self):
        return "%s" % (self.name)

# TODO: ADD SUBSCRIPTION EXTENSION MODEL

class Subscription(models.Model):
    registration_date = models.DateField()
    description = models.CharField(('Description'), max_length=300, blank=True, default='')
    subscription_type = models.ForeignKey('SubscriptionCategory', related_name='subscriptions', on_delete=models.CASCADE)
    payment = models.ForeignKey('Payment', related_name='subscription', on_delete=models.CASCADE)

    member = models.ForeignKey('Member', 
        on_delete = models.CASCADE,
        related_name='subscriptions',
        help_text='Subscriptions that the member has'
    )

    class Meta:
         verbose_name = 'Subscription'
         verbose_name_plural = 'Subscriptions'
         ordering = ('-registration_date',)

    def __str__(self):
        return "#%s – (%s)" % (self.id, self.registration_date)

class SubscriptionVisit(models.Model):
    date = models.DateField()
    group = models.ForeignKey('Group', related_name='subscription_visits', on_delete=models.CASCADE)

    subscription = models.ForeignKey('Subscription',
        on_delete=models.CASCADE,
        blank=False,
        related_name='visits',
        help_text='A visit based on a subscription')

    class Meta:
        verbose_name = 'Subscription Visit'
        verbose_name_plural = 'subscription Visits'

    def __str__(self):
        return "%s" % (self.group)

class SingleVisit(models.Model):
    date = models.DateField()
    payment = models.ForeignKey('Payment', related_name='single_visit', on_delete=models.CASCADE)
    group = models.ForeignKey('Group', related_name='single_visits', on_delete=models.CASCADE)

    member = models.ForeignKey('Member', 
        on_delete = models.CASCADE,
        related_name='single_visits',
        help_text='Single visits that the member has made'
    )

    class Meta:
        verbose_name = 'Single Visit'
        verbose_name_plural = 'Single Visits'
        ordering = ('-date',)

    def __str__(self):
        return "%s" % (self.payment)

class ItemPurchase(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=30)
    payment = models.ForeignKey('Payment', related_name='item_purchases', on_delete=models.CASCADE)

    member = models.ForeignKey('Member', 
        on_delete = models.CASCADE,
        related_name='item_purchases',
        help_text='Item purchases that the member has made'
    )

    # item_purchse_payment = models.OneToOneField('Payment', null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Item Purchase'
        verbose_name_plural = 'Item Purchases'

    def __str__(self):
        return "%s" % (self.first_name, self.last.name)





