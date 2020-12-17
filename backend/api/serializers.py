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
    category = serializers.SlugRelatedField(
        slug_field="last_name",
        read_only=True
    )

    class Meta:
        model = Instructor
        exclude = [
        ]

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        exclude = [
        ]
