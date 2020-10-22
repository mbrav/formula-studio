from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Member, Subscription, SubscriptionType
from rest_framework import viewsets
from .serializers import MemberSerializer

class MemberViewSet(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()
