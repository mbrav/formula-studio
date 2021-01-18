from django.urls import path, include
from . import views
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('groups', GroupViewSet, basename='groups')
router.register('instructors', InstructorViewSet, basename='instructors')
router.register('members', MemberViewSet, basename='members')
router.register('signups', SignupViewSet, basename='signups')
router.register('payments', PaymentViewSet, basename='payments')
router.register('subscriptions', SubscriptionViewSet, basename='subscriptions')
router.register('subscription-visits', SubscriptionVisitViewSet, basename='subscription-visits')
router.register('single-visits', SingleVisitViewSet, basename='single-visits')
router.register('purchases', ItemPurchaseViewSet, basename='purchases')

urlpatterns = [
    path('', include(router.urls)),
]

# DEBUG
# for url in router.urls:
#     print(url, '\n')
