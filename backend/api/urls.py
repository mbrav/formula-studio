from django.urls import path, include
from . import views
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('groups', GroupViewSet, basename='groups')
router.register('signups', SignupViewSet, basename='signups')
router.register('instructors', InstructorViewSet, basename='instructors')

urlpatterns = [
    path('', include(router.urls)),
    # path('groupsearch/', views.GroupSearchViewSet.as_view())
]

# DEBUG
# for url in router.urls:
#     print(url, '\n')
