from django.urls import path
from . import views

urlpatterns = [
    path('reviews', views.reviews),
    path('list', views.list)
]
