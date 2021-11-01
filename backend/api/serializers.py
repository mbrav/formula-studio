from rest_framework import serializers

from formula_studio.models import *


class BasicGroupCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = GroupCategory
        exclude = [
        ]


class BasicGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        exclude = [
        ]


class FullGroupSerializer(BasicGroupSerializer):

    revenue = serializers.SerializerMethodField(
        method_name='get_revenue')
    visits = serializers.SerializerMethodField(
        method_name='get_visits_total')

    def get_revenue(self, obj):
        """Calculate revenue stats for Group"""

        money_sum = 0
        for sub_v in obj.subscription_visits.all():
            # Get average price of subscription visit by dividing
            # its price by number of visits to get average
            if not sub_v.subscription.payment.writen_off:
                money_sum += (sub_v.subscription.payment.amount /
                              sub_v.subscription.subscription_category.number_of_visits)
        for single_v in obj.single_visits.all():
            if not single_v.payment.writen_off:
                money_sum += single_v.payment.amount
        return money_sum

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


class BasicInstructorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Instructor
        exclude = [
        ]


class FullInstructorSerializer(BasicInstructorSerializer):
    revenue = serializers.SerializerMethodField(
        method_name='get_revenue')

    def get_revenue(self, obj):
        """Calculate revenue stats for Instructor"""

        money_sum = 0
        for group in obj.groups.all():
            # Count subs
            for sub_v in group.subscription_visits.all():
                if not sub_v.subscription.payment.writen_off:
                    money_sum += (sub_v.subscription.payment.amount /
                                  sub_v.subscription.subscription_category.number_of_visits)
            # Count single visits
            for single_v in group.single_visits.all():
                if not single_v.payment.writen_off:
                    money_sum += single_v.payment.amount
        return money_sum

    class Meta:
        model = Instructor
        read_only_fields = ('revenue',)
        exclude = [
        ]


class BasicMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        exclude = [
        ]


class FullMemberSerializer(serializers.ModelSerializer):

    revenue = serializers.SerializerMethodField(
        method_name='get_revenue')
    visits = serializers.SerializerMethodField(
        method_name='get_visits_total')

    def get_revenue(self, obj):
        """Calculate revenue stats for Member"""
        money_sum = 0
        for sub in obj.subscriptions.all():
            if not sub.payment.writen_off:
                for sub_v in sub.subscription_visits.all():
                    money_sum += (sub_v.subscription.payment.amount /
                                  sub_v.subscription.subscription_category.number_of_visits)
        # Count single visits
        for single_v in obj.single_visits.all():
            if not single_v.payment.writen_off:
                money_sum += single_v.payment.amount
        return money_sum

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


class BasicSignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Signup
        exclude = [
        ]


class BasicPaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        exclude = [
        ]


class BasicSubscriptionSerializer(serializers.ModelSerializer):

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


class BasicSubscriptionVisitSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubscriptionVisit
        exclude = [
        ]


class BasicSingleVisitSerializer(serializers.ModelSerializer):

    class Meta:
        model = SingleVisit
        exclude = [
        ]


class BasicItemPurchaseSerializer(serializers.ModelSerializer):

    item_category = serializers.SlugRelatedField(
        slug_field="name",
        read_only=True
    )

    class Meta:
        model = ItemPurchase
        exclude = [
        ]
