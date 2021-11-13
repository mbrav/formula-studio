from django.urls import include, path
from rest_framework import routers

from . import views
from .views import *

router = routers.DefaultRouter()
router.register('class-categories', EventCategoryViewSet,
                basename='class_categories')
router.register(r'class-categories/(?P<cat_id>\d+)/',
                ScheduleEventViewSet, basename='class_category')
router.register('classes', ScheduleEventViewSet, basename='classes')
router.register(r'classes/(?P<class_id>\d+)/signups',
                SignupViewSet, basename='class_signups')

router.register('instructors', InstructorViewSet, basename='instructors')
router.register(r'instructors/(?P<user_id>\d+)/classes',
                ScheduleEventViewSet, basename='instructor_classes')

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
