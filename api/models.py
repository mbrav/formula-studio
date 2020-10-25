from django.db import models
from django import forms

# Create your models here.

class Member(models.Model):
    first_name = models.CharField(('First Name'), max_length=50)
    last_name = models.CharField(('Last Name'), max_length=50)
    mobile_number = models.CharField(('Mobile Number'), max_length=10, unique=True, blank=False)
    email = models.EmailField(null=True, blank=True, unique=True)
    description = models.CharField(('Description'), max_length=300, blank=True, default='description...')
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

    payment_date = models.DateField(auto_now_add=True)

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

    # single_visit = models.ForeignKey('SingleVisit', related_name='single_visit', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
        ordering = ('-payment_date',)

    def __str__(self):
        return "#%s – (%s)" % (self.id, self.payment_date)

# TODO: ADD ENCASHMENT MODEL

class SubscriptionType(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(('Description'), max_length=300, blank=True, default='description...')
    number_of_visits = models.PositiveIntegerField(blank=False, null=False)
    validity_in_days = models.PositiveIntegerField(blank=False, null=False)

    class Meta:
        verbose_name = 'Subscription type'
        verbose_name_plural = 'Subscription types'
        ordering = ('-name',)

    def __str__(self):
        return "%s" % (self.name)

class Subscription(Payment):
    registration_date = models.DateField(auto_now_add=True)
    description = models.CharField(('Description'), max_length=300, blank=True, default='description...')
    subscription_type = models.OneToOneField('SubscriptionType', null=False, blank=False, on_delete=models.CASCADE)
    # TODO: ADD SUBSCRIPTION EXTENSION MODEL

    class Meta:
         verbose_name = 'Subscription'
         verbose_name_plural = 'Subscriptions'
         ordering = ('-registration_date',)


    def __str__(self):
        return "#%s – (%s)" % (self.id, self.registration_date)

class SingleVisit(Payment):
    date = models.DateField(auto_now_add=True)
    
    # payment = models.OneToOneField('Payment', null=False, blank=False, on_delete=models.CASCADE)

    # group = models.ForeignKey('Subscription',
    #     on_delete=models.CASCADE,
    #     blank=False,
    #     related_name='visits',
    #     help_text='A single visit)

    class Meta:
        verbose_name = 'Single visit'
        verbose_name_plural = 'Single visits'
        ordering = ('-date',)

    def __str__(self):
        return "%s" % (self.payment)

class ItemPurchase(Payment):
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Visit'
        verbose_name_plural = 'Visits'

    def __str__(self):
        return "%s" % (self.first_name, self.last.name)

class GroupCategory():
    name = models.CharField(max_length=30)
    description = models.CharField(('Description'), max_length=300, blank=True, default='description...')

    class Meta:
        verbose_name = 'Group category'
        verbose_name_plural = 'Group categories'


    def __str__(self):
        return "%s" % (self.name)

class Group():
    name = models.CharField(max_length=30)
    category = models.OneToOneField('GroupCategory', null=False, blank=False, on_delete=models.CASCADE)

    # TODO: ADD INSTRUCTOR / USER (?) MODEL

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

    def __str__(self):
        return "%s" % (self.name)

# VISIT IS NOW SUBSCRIPTION VISIT - TO RENAME
    
class Visit(models.Model):
    date = models.DateField()
    # group = models.OneToOneField('Group', null=False, blank=False, on_delete=models.CASCADE)

    subscription = models.ForeignKey('Subscription',
        on_delete=models.CASCADE,
        blank=False,
        related_name='visits',
        help_text='A visit based on a subscription')

    class Meta:
        verbose_name = 'Subscription visit'
        verbose_name_plural = 'subscription visits'

    def __str__(self):
        return "%s" % (self.first_name, self.last.name)




