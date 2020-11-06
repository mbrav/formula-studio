from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from .models import Member, Group, Signup
from .serializers import MemberSerializer, GroupSerializer, SignupSerializer

class MemberViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = MemberSerializer
    queryset = Member.objects.all()

class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

class SignupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SignupSerializer
    queryset = Signup.objects.all()

    @action(detail=True, methods=['GET'])
    def add(self, request, pk=None):
        response = {
            'message' : 'its working'
        }
        return Response(response, status=status.HTTP_201_CREATED) 

