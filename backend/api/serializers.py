from rest_framework import serializers
from .models import *


class GroupSerializer(serializers.ModelSerializer):

    revenue = serializers.SerializerMethodField(
        method_name='get_revenue')
    visits = serializers.SerializerMethodField(
        method_name='get_visits_total')

    def get_revenue(self, obj):
        """Calculate revenue stats for Group"""
        money = 0
        for sub_v in obj.subscription_visits.all():
            # Get average price of subscription visit by dividing
            # its price by number of visits to get average
            if not sub_v.subscription.payment.writen_off:
                money += (sub_v.subscription.payment.amount /
                          sub_v.subscription.subscription_category.number_of_visits)
        for single_v in obj.single_visits.all():
            if not single_v.payment.writen_off:
                money += single_v.payment.amount
        return money

    def get_visits_total(self, obj):
        """Count class visit stats for Group"""

        visits = 0
        for sub_v in obj.subscription_visits.all():
            visits += 1
        for single_v in obj.single_visits.all():
            visits += 1
        return visits

    class Meta:
        model = Group
        read_only_fields = ('revenue', 'visits')
        exclude = [
        ]


class InstructorSerializer(serializers.ModelSerializer):
    revenue = serializers.SerializerMethodField(
        method_name='get_revenue')

    def get_revenue(self, obj):
        """Calculate revenue stats for Instructor"""
        money = 0
        for group in obj.groups.all():
            # Count subs
            for sub_v in group.subscription_visits.all():
                if not sub_v.subscription.payment.writen_off:
                    money += (sub_v.subscription.payment.amount /
                              sub_v.subscription.subscription_category.number_of_visits)
            # Count single visits
            for single_v in group.single_visits.all():
                if not single_v.payment.writen_off:
                    money += single_v.payment.amount
        return money

    class Meta:
        model = Instructor
        read_only_fields = ('revenue',)
        exclude = [
        ]


class MemberSerializer(serializers.ModelSerializer):

    revenue = serializers.SerializerMethodField(
        method_name='get_revenue')
    visits = serializers.SerializerMethodField(
        method_name='get_visits_total')

    def get_revenue(self, obj):
        """Calculate revenue stats for Member"""
        money = 0
        for sub in obj.subscriptions.all():
            if not sub.payment.writen_off:
                for sub_v in sub.subscription_visits.all():
                    money += (sub_v.subscription.payment.amount /
                              sub_v.subscription.subscription_category.number_of_visits)
        # Count single visits
        for single_v in obj.single_visits.all():
            if not single_v.payment.writen_off:
                money += single_v.payment.amount
        return money

    def get_visits_total(self, obj):
        """Count class visit stats for the Member"""

        visits = 0
        for sub in obj.subscriptions.all():
            for sub_visit in sub.subscription_visits.all():
                visits += 1
        for single_v in obj.single_visits.all():
            visits += 1
        return visits

    class Meta:
        model = Member
        read_only_fields = ('visits', 'revenue')
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

    visits_total = serializers.SerializerMethodField(
        method_name='get_visits_total')
    visits_made = serializers.SerializerMethodField(
        method_name='get_visits_made')
    visits_remaining = serializers.SerializerMethodField(
        method_name='get_visits_remaining')

    def get_visits_total(self, obj):
        return obj.subscription_category.number_of_visits

    def get_visits_made(self, obj):
        return obj.subscription_visits.all().count()

    def get_visits_remaining(self, obj):
        return (
            obj.subscription_category.number_of_visits -
            obj.subscription_visits.all().count()
        )

    class Meta:
        model = Subscription
        read_only_fields = ('visits', 'revenue', 'visits_remaining')
        exclude = [
        ]


class SubscriptionVisitSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubscriptionVisit
        exclude = [
        ]


class SingleVisitSerializer(serializers.ModelSerializer):

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
