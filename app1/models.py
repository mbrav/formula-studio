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

    member = models.ForeignKey('Member', on_delete=models.CASCADE)

    def __str__(self):
        return "#%s – (%s)" % (self.id, self.payment_date)

class SubscriptionType(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10, blank=True)
    description = models.CharField(('Subscription'), max_length=300, blank=True, default='description...')

    def __str__(self):
        return "%s" % (self.name)

class Subscription(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular subscription")
    registration_date = models.DateField()
    description = models.CharField(('Description'), max_length=300, blank=True, default='description...')

    payment = models.OneToOneField(Payment, null=False, blank=False, on_delete=models.CASCADE)

    member = models.ForeignKey('Member', 
        on_delete = models.CASCADE,
        related_name='subscriptions',
        help_text='Member to which this subscription is assigned'
    )

    subscription_type = models.ForeignKey('SubscriptionType',
        on_delete=models.CASCADE,
        blank=False,
        related_name='subscription_type',
        help_text='Select a subscription type') 

    def __str__(self):
        return "#%s – (%s)" % (self.id, self.registration_date)



