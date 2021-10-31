from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from formula_studio.models import *
from .serializers import *


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    search_fields = [
        'instructor__id',
    ]

    filter_backends = (filters.SearchFilter,)
    queryset = Group.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return FullGroupSerializer
        return BasicGroupSerializer


class InstructorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    search_fields = [
        'id',
        'first_name',
        'last_name',
    ]

    filter_backends = (filters.SearchFilter,)
    queryset = Instructor.objects.all()
    serializer_class = BasicInstructorSerializer


class MemberViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    search_fields = [
        'id',
        'first_name',
        'last_name',
    ]

    filter_backends = (filters.SearchFilter,)
    queryset = Member.objects.all()
    serializer_class = BasicMemberSerializer


class SignupViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    search_fields = [
        'id',
        'member',
        'subscription_category',
    ]

    filter_backends = (filters.SearchFilter,)
    queryset = Signup.objects.all()
    serializer_class = BasicSignupSerializer

    # Process signup with a set of lookups with available info
    # Necessary for implementating signups without login functionality
    # While not relying on login fucntionality
    def create(self, request, *args, **kwargs):

        # set request data to mutable
        # https://stackoverflow.com/questions/44717442/
        request.data._mutable = True

        group_name = None
        # check if google calendar id was profvided, if not, retruns False
        cal_id_provided = request.POST.get('group_google_cal_id', False)
        if cal_id_provided != False:
            if Group.objects.filter(google_cal_id=request.POST['group_google_cal_id']).exists():
                group = Group.objects.filter(
                    google_cal_id=request.POST['group_google_cal_id'])
                group_name = group[0].name
                request.POST['group'] = group[0].id
            else:
                group_name = "lookup fail"
        else:
            group_name = "lookup fail"

        # Process request with provided data and try to assign it to and an existing entry in the database

        # Empty Dictionaries Checks
        member_name_first = None
        member_name_last = None
        name = []
        name_provided_first = request.POST.get('first_name', False)
        name_provided_last = request.POST.get('last_name', False)
        if name_provided_last != False and name_provided_first != False:
            member_name_first = request.POST['first_name']
            member_name_last = request.POST['last_name']
            name = Member.objects.filter(
                first_name=member_name_first,
                last_name=member_name_last
            )
        else:
            member_name_last = "lookup fail"

        phone_num = None
        phone = []
        phone_num_provided = request.POST.get('mobile_number', False)
        if phone_num_provided != False:
            phone_num = request.POST['mobile_number']
            phone = Member.objects.filter(mobile_number=phone_num)
        else:
            phone_num = "lookup fail"

        e_mail = None
        email = []
        e_mail_provided = request.POST.get('email', False)
        if e_mail_provided != False:
            e_mail = request.POST['email']
            email = Member.objects.filter(email=e_mail)
        else:
            e_mail = "lookup fail"

        member_id = None
        # Name check
        if len(name) > 0:
            request.POST['member'] = name[0].id
            member_id = name[0].id

        # Mobile number check
        elif len(phone) > 0:
            request.POST['member'] = phone[0].id
            member_id = phone[0].id
            member_name_last = "double lookup fail"

        # Email check
        elif len(email) > 0:
            request.POST['member'] = email[0].id
            member_id = email[0].id
            phone_num = "double lookup fail"

        else:
            request.POST['member'] = 2  # default member
            e_mail = "double lookup fail"

        # End Request mutations
        request.data._mutable = False

        # Validate Serializer
        serializer = self.get_serializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        response = {
            'success': 'True',
            'group_assigned': group_name,
            'member_id_assigned': member_id,
            'name_lookup': member_name_last,
            'phone_lookup': phone_num,
            'email_lookup': e_mail
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
    serializer_class = BasicPaymentSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    search_fields = [
        'id',
    ]

    filter_backends = (filters.SearchFilter,)
    queryset = Subscription.objects.all()
    serializer_class = BasicSubscriptionSerializer


class SubscriptionVisitViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    search_fields = [
        'id',
    ]

    filter_backends = (filters.SearchFilter,)
    queryset = SubscriptionVisit.objects.all()
    serializer_class = BasicSubscriptionVisitSerializer


class SingleVisitViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    search_fields = [
        'id',
    ]

    filter_backends = (filters.SearchFilter,)
    queryset = SingleVisit.objects.all()
    serializer_class = BasicSingleVisitSerializer


class ItemPurchaseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    search_fields = [
        'id',
    ]

    filter_backends = (filters.SearchFilter,)
    queryset = ItemPurchase.objects.all()
    serializer_class = BasicItemPurchaseSerializer
