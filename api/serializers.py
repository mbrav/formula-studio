from rest_framework import serializers
from .models import Member, Payment, SingleVisit, Subscription, SubscriptionType

class SubscriptionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionType
        fields = ['id', 'name', 'price', 'description']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            'id', 
            'payment_date', 
            'payment_amount', 
            'payment_type', 
            'payment_paid',
            'member'
        ]

class SingleVisitSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(many = False)
    class Meta:
        model = SingleVisit
        fields = ['id',
            'name',
            'payment',
            'member',
        ]

class SubscriptionSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(many = False)
    class Meta:
        model = Subscription
        fields = ['id',
            'registration_date',
            'member',
            'subscription_type',
            'payment'
        ]

class MemberSerializer(serializers.ModelSerializer):
    subscriptions = SubscriptionSerializer(many = True)
    single_visits = SingleVisitSerializer(many = True)
    class Meta:
        model = Member
        fields = ['id', 
            'first_name',
            'last_name',
            'mobile_number',
            'email',
            'registered_on',
            'description',
            'single_visits',
            'subscriptions',
        ]