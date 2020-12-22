from django.urls import path, re_path, include
from . import views
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('groups', GroupViewSet, basename='groups')
router.register('signups', SignupViewSet)
router.register('instructors', InstructorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

for url in router.urls:
    print(url, '\n')
