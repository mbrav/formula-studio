from rest_framework import serializers
from .models import Member, Payment, SingleVisit, Subscription, SubscriptionVisit, SubscriptionCategory

class SubscriptionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionCategory
        fields = ['id', 'name', 'price', 'description']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            'id', 
            'date', 
            'amount', 
            'method', 
            'paid',
            'member'
        ]

class SingleVisitSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(many = False)
    class Meta:
        model = SingleVisit
        fields = ['id',
            'date',
            'payment',
            'member',
        ]

class SubscriptionVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleVisit
        fields = ['id',
            'date',
            'group'
        ]

class SubscriptionSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(many = False)
    visits = SubscriptionVisitSerializer(many = True)
    class Meta:
        model = Subscription
        fields = ['id',
            'registration_date',
            'member',
            'subscription_type',
            'payment',
            'visits_made',
            'visits'
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