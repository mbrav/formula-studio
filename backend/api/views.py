from rest_framework import viewsets, generics, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from .models import *
from .serializers import *

class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    search_fields = [
        'instructor__id',
    ]

    filter_backends = (filters.SearchFilter,)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class InstructorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    search_fields = [
        'id',
        'first_name',
        'last_name',
    ]

    filter_backends = (filters.SearchFilter,)
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class SignupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    search_fields = [
        'id',
        'first_name',
        'last_name',
    ]

    filter_backends = (filters.SearchFilter,)
    queryset = Signup.objects.all()
    serializer_class = SignupSerializer
