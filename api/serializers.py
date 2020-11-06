from rest_framework import serializers
from .models import Signup, Group
        
        # fields = [
        #     'id', 
        #     'name', 
        #     'price', 
        #     'description'
        # ]


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

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        exclude = [
        ]