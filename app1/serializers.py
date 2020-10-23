from rest_framework import serializers
from .models import Member, Subscription, SubscriptionType

class SubscriptionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionType
        fields = ['id', 'name', 'price', 'description']

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 
                #   'registration_date',
                  'member', 
                #   'fee_status',
                  'subscription_type']

class MemberSerializer(serializers.ModelSerializer):
    subscriptions = SubscriptionSerializer(many = True)
    class Meta:
        model = Member
        fields = ['id', 
                  'first_name',
                  'last_name', 
                  'mobile_number', 
                  'email',
                #   'registered_on',
                  'subscriptions',
                  'description']