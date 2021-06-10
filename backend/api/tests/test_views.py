from django.test import TestCase
from django.conf import settings

from rest_framework import viewsets, generics, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from .models import *
from .serializers import *


class CalTest(LiveServerTestCase):
    fixtures = ["init.json"]
