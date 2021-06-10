from rest_framework import viewsets, generics, filters, status
from rest_framework.response import Response
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
    permission_classes = [IsAuthenticated]

    search_fields = [
        'id',
        'first_name',
        'last_name',
    ]

    filter_backends = (filters.SearchFilter,)
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class SignupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    search_fields = [
        'id',
        'member',
        'subscription_category',
    ]

    filter_backends = (filters.SearchFilter,)
    queryset = Signup.objects.all()
    serializer_class = SignupSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        google_event_status = ""
        # check if google calendar id was profvided, if not, retruns False
        google_id_provided = request.POST.get('group_google_cal_id"', False)
        if google_id_provided != False:
            group = Group.objects.get(
                google_cal_id=request.POST['group_google_cal_id'])
            if group is True:
                google_event_status = status.HTTP_200_OK
            else:
                google_event_status = status.HTTP_206_PARTIAL_CONTENT
        else:
            google_event_status = status.HTTP_204_NO_CONTENT

        response = {
            'success': 'True',
            'google_event': google_event_status,
        }

        status_code = status.HTTP_200_OK
        return Response(response, status=status_code)

        def perform_create(self, serializer):
            serializer.save()

        def get_success_headers(self, data):
            try:
                return {'Location': str(data[api_settings.URL_FIELD_NAME])}
            except (TypeError, KeyError):
                return {}


class PaymentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    search_fields = [
        'id',
        'member',
    ]

    filter_backends = (filters.SearchFilter,)
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    search_fields = [
        'id',
    ]

    filter_backends = (filters.SearchFilter,)
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class SubscriptionVisitViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    search_fields = [
        'id',
    ]

    filter_backends = (filters.SearchFilter,)
    queryset = SubscriptionVisit.objects.all()
    serializer_class = SubscriptionVisitSerializer


class SingleVisitViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    search_fields = [
        'id',
    ]

    filter_backends = (filters.SearchFilter,)
    queryset = SingleVisit.objects.all()
    serializer_class = SingleVisitSerializer


class ItemPurchaseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    search_fields = [
        'id',
    ]

    filter_backends = (filters.SearchFilter,)
    queryset = ItemPurchase.objects.all()
    serializer_class = ItemPurchaseSerializer
