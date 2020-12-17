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

    @action(detail=False, methods=['GET'])
    def info(self, request):
        count_total = Instructor.objects.all().count()
        response = {
            'countTotal' : count_total
        }
        return Response(response, status=status.HTTP_200_OK)

class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

    @action(detail=False, methods=['GET'])
    def info(self, request):
        count_total = Group.objects.all().count()
        response = {
            'countTotal' : count_total
        }
        return Response(response, status=status.HTTP_200_OK)

class SignupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = SignupSerializer
    queryset = Signup.objects.all()

    @action(detail=False, methods=['GET'])
    def info(self, request):
        count_total = Signup.objects.all().count()
        response = {
            'countTotal' : count_total
        }
        return Response(response, status=status.HTTP_200_OK)
