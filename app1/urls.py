from django.urls import path, include
# from . import views
# from .views import Another
from .views import BookViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    # path('list', Another.as_view()),
    # path('', views.main),
    path('', include(router.urls)),
]
