from django.urls import path, include
# from . import views
# from .views import Another
from .views import MemberViewSet, GroupViewSet, SignupViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('members', MemberViewSet)
router.register('groups', GroupViewSet)
router.register('signups', SignupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
