from django.urls import path
from . import views
from .views import Another

urlpatterns = [
    path('list', Another.as_view()),
    path('', views.main),
]
