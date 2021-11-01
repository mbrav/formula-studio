from django.urls import include, path
from rest_framework import routers

from . import views
from .views import *

router = routers.DefaultRouter()
router.register('group-categories', GroupCategoryViewSet,
                basename='group_categories')
router.register(r'group-categories/(?P<cat_id>\d+)/',
                GroupViewSet, basename='group_category')
router.register('groups', GroupViewSet, basename='groups')
router.register(r'groups/(?P<group_id>\d+)/signups',
                SignupViewSet, basename='group_signups')

router.register('instructors', InstructorViewSet, basename='instructors')
router.register(r'instructors/(?P<user_id>\d+)/groups',
                GroupViewSet, basename='instructor_groups')

router.register('members', MemberViewSet, basename='members')
router.register('signups', SignupViewSet, basename='signups')
router.register('payments', PaymentViewSet, basename='payments')

router.register('subscriptions', SubscriptionViewSet, basename='subscriptions')
router.register(r'subscriptions/(?P<sub_id>\d+)/visits',
                SubscriptionVisitViewSet, basename='subscription-visits')

router.register('single-visits', SingleVisitViewSet, basename='single-visits')
router.register('purchases', ItemPurchaseViewSet, basename='purchases')

urlpatterns = [
    path('', include(router.urls)),
]

# DEBUG
# for url in router.urls:
#     print(url, '\n')
