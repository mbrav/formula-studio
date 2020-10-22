from django.db import models
from django import forms

FEE_STATUS = (
    ('paid', 'Paid'),
    ('pending', 'Pending'),
)

# Create your models here.

class Member(models.Model):
    first_name = models.CharField(('First Name'), max_length=50)
    last_name = models.CharField(('Last Name'), max_length=50)
    mobile_number = models.CharField(('Mobile Number'), max_length=10, unique=True)
    email = models.EmailField(null=True, blank=True, unique=True)
    description = models.CharField(('Description'), max_length=300, blank=True, default='None')
    registered_on = models.DateField(auto_now_add=True)

    image = models.ImageField(upload_to='img/member_profiles', blank=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class SubscriptionType(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10, blank=True)
    description = models.CharField(('Description'), max_length=300, blank=True, default='None')

    def __str__(self):
        return "%s" % (self.name)

class Subscription(models.Model):
    registration_date = forms.DateField()
    fee_status = forms.ChoiceField(choices=FEE_STATUS)
    description = models.CharField(('Description'), max_length=300, blank=True, default='None')

    member = models.ForeignKey(Member, on_delete = models.CASCADE, related_name='subscriptions')
    subscription_type = models.ManyToManyField(SubscriptionType, related_name='type')

    def __str__(self):
        return "%s" % (self.id)


