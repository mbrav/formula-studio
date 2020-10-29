from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets
from .models import Member, Group
from .serializers import MemberSerializer, GroupSerializer

class MemberViewSet(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()

class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
