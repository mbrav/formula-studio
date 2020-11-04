from rest_framework import serializers
from .models import Member, Payment, SingleVisit, Subscription, SubscriptionVisit, SubscriptionCategory, Group

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
            'writen_off',
        ]

class SingleVisitSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(many = False)
    class Meta:
        model = SingleVisit
        fields = ['id',
            'date',
            'payment',
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
    subscription_visits = SubscriptionVisitSerializer(many = True)
    class Meta:
        model = Subscription
        fields = ['id',
            'registration_date',
            'subscription_category',
            'payment',
            'visits_total',
            'visits_made',
            'visits_remaining',
            'subscription_visits'
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

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 
            'category',
            'name',
            'revenue',
            'visits_total',
        ]