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

class MemberViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    search_fields = [
        'id',
        'first_name',
        'last_name',
    ]

    filter_backends = (filters.SearchFilter,)
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class SignupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    search_fields = [
        'id',
        'member',
        'subscription_category',
    ]

    filter_backends = (filters.SearchFilter,)
    queryset = Signup.objects.all()
    serializer_class = SignupSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    search_fields = [
        'id',
    ]

    filter_backends = (filters.SearchFilter,)
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

class SubscriptionVisitViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    search_fields = [
        'id',
    ]

    filter_backends = (filters.SearchFilter,)
    queryset = SubscriptionVisit.objects.all()
    serializer_class = SubscriptionVisitSerializer

class SingleVisitViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    search_fields = [
        'id',
    ]

    filter_backends = (filters.SearchFilter,)
    queryset = SingleVisit.objects.all()
    serializer_class = SingleVisitSerializer

class ItemPurchaseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    search_fields = [
        'id',
    ]

    filter_backends = (filters.SearchFilter,)
    queryset = ItemPurchase.objects.all()
    serializer_class = ItemPurchaseSerializer
