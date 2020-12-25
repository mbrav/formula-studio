from rest_framework import serializers
from .models import *

# payment = serializers.SlugRelatedField(slug_field="date", read_only=True)
# subscription_visits = SubscriptionVisitSerializer(many = True)

class GroupSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field="name",
        read_only=True
    )

    class Meta:
        model = Group
        exclude = [
        ]

class InstructorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instructor
        exclude = [
        ]

class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        exclude = [
        ]

class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Signup
        exclude = [
        ]

class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        exclude = [
        ]

class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        exclude = [
        ]

class SubscriptionVisitSerializer(serializers.ModelSerializer):

    group = serializers.SlugRelatedField(
        slug_field="name",
        read_only=True
    )

    class Meta:
        model = SubscriptionVisit
        exclude = [
        ]

class SingleVisitSerializer(serializers.ModelSerializer):

    group = serializers.SlugRelatedField(
        slug_field="name",
        read_only=True
    )

    class Meta:
        model = SingleVisit
        exclude = [
        ]

class ItemPurchaseSerializer(serializers.ModelSerializer):

    item_category = serializers.SlugRelatedField(
        slug_field="name",
        read_only=True
    )

    class Meta:
        model = ItemPurchase
        exclude = [
        ]
