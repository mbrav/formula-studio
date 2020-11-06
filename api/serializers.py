from rest_framework import serializers
from .models import Member, Signup, Payment, SingleVisit, Subscription, SubscriptionVisit, SubscriptionCategory, Group

class SubscriptionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionCategory
        fields = [
            'id', 
            'name', 
            'price', 
            'description'
        ]

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        exclude = [
            'writen_off',
        ]

class SingleVisitSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(many = False)
    class Meta:
        model = SingleVisit

class SubscriptionVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleVisit

class SubscriptionSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(many = False)
    # payment = serializers.SlugRelatedField(slug_field="date", read_only=True)
    subscription_visits = SubscriptionVisitSerializer(many = True)
    class Meta:
        model = Subscription

class MemberSerializer(serializers.ModelSerializer):
    subscriptions = SubscriptionSerializer(many = True)
    single_visits = SingleVisitSerializer(many = True)
    class Meta:
        model = Member

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup