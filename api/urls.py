from django.urls import path, include
# from . import views
# from .views import Another
from .views import MemberViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('members', MemberViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
