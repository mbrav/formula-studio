from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from .models import *
from .serializers import *

class InstructorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()

class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

    @action(methods=['get'], detail=False)
    def get(self, request):
        newest = self.get_queryset().order_by('date').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)

class SignupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SignupSerializer
    queryset = Signup.objects.all()
