from rest_framework import serializers
from .models import Member, Subscription, SubscriptionType

class SubscriptionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionType
        fields = ['id', 'name', 'price', 'description', 'subscription_type']

class SubscriptionSerializer(serializers.ModelSerializer):
    subscription_type = SubscriptionTypeSerializer(many = False)
    class Meta:
        model = Subscription
        fields = ['id', 
                  'member', 
                #   'registration_date',
                  'subscription_type', 
                  'fee_status']

class MemberSerializer(serializers.ModelSerializer):
    subscriptions = SubscriptionSerializer(many = True)
    class Meta:
        model = Member
        fields = ['id', 
                  'first_name',
                  'last_name', 
                  'mobile_number', 
                  'email',
                  'subscriptions',
                #   'registered_on',
                  'description']
