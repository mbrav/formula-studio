from rest_framework import serializers
from .models import Member, Subscription, SubscriptionType

class SubscriptionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionType
        fields = ['id', 'name', 'price', 'subscription_type']

class SubscriptionSerializer(serializers.ModelSerializer):
    typeof = SubscriptionTypeSerializer(many = False)
    class Meta:
        model = Subscription
        fields = ['id', 'registration_date','typeof', 'fee_status']

class MemberSerializer(serializers.ModelSerializer):
    subscriptions = SubscriptionSerializer(many = True)
    class Meta:
        model = Member
        fields = ['id', 'first_name', 'last_name', 'mobile_number', 'email', 'subscriptions', 'description', 'registered_on']
