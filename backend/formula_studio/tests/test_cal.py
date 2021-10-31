from django.test import TestCase, LiveServerTestCase
from formula_studio.models import Group, GroupCategory, Instructor
from django.conf import settings

import datetime
from dateutil.relativedelta import relativedelta
import pytz
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

local_timezone = pytz.timezone(settings.TIME_ZONE)
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
base_test_dir = 'api/tests/'


class CalTest(LiveServerTestCase):
    fixtures = ["init.json"]

    def get(self):
        """Shows basic usage of the Google Calendar API.
        Prints the start and name of the next 10 events on the user's calendar.
        """
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(base_test_dir + 'token.json'):
            creds = Credentials.from_authorized_user_file(
                base_test_dir + 'token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    base_test_dir + 'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(base_test_dir + 'token.json', 'w') as token:
                token.write(creds.to_json())

        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.now() + relativedelta(months=-1)
        now = now.isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Fetching events')

        events_result = service.events().list(calendarId=settings.GOOGLE_CALENDAR_ID,
                                              timeMin=now, maxResults=10000, singleEvents=True, orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No events found.')
        else:
            print('Fetched', len(events), 'events')

        return events

    def save(self):
        events = self.get()
        file = open(base_test_dir + 'event-list.csv', 'w')
        for event in events:
            id = event['id']
            start = event['start'].get('dateTime', event['start'].get('date'))
            file.write(id + ", " + str(start) + ", " +
                       str(event['summary']) + "\n")
        file.close()

    def create(self):
        events = self.get()
        instruct = Instructor.objects.get(pk=1)
        group_category = GroupCategory.objects.get(pk=1)
        for event in events:
            id = event['id']
            if not Group.objects.filter(google_cal_id=id):
                event_date = event['start'].get('dateTime')
                print("Event does not exist, creating: ",
                      event['summary'], event_date)
                new_group = Group(
                    google_cal_id=id,
                    name=event['summary'],
                    date=event_date,
                    category=group_category,
                    instructor=instruct
                )
                new_group.save()

        print(Group.objects.get(pk=9).name)
        print(Group.objects.get(pk=9).category)
        # Django stores dates in UTC when USE_TZ = True in settings
        # Hence conversion is necessary
        dt_ts = Group.objects.get(pk=9).date.replace(
            tzinfo=pytz.utc).astimezone(local_timezone)
        print(dt_ts)
        print(Group.objects.get(pk=9).google_cal_id)
        print(Group.objects.get(pk=9).instructor)

    def update(self):
        events = self.get()
        self.create()
        for event in events:
            id = event['id']
            group_db = Group.objects.get(google_cal_id=id)
            event_date = datetime.datetime.fromisoformat(
                event['start'].get('dateTime', event['start'].get('date')))

            # Django stores dates in UTC when USE_TZ = True in settings
            # Hence conversion is necessary, but when saving, Django handles things automatically
            # https://stackoverflow.com/a/14714819
            group_db_local_date = group_db.date.replace(
                tzinfo=pytz.utc).astimezone(local_timezone)

            if group_db_local_date != event_date:
                print("Event time change, updating time",
                      group_db_local_date, event_date)
                group_db.date = event_date
                group_db.save()

# To run on a docker compose do:
# docker-compose run app sh -c "python manage.py test"

# Test functions


def add(x, y):
    """Add two numbers"""
    return x + y


def subtract(x, y):
    """Subtract two numbers"""
    return y - x

# Run tests


class CalcTestCase(TestCase):

    def test_num(self):
        """Test that nums are added"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """Test that nums are subtracted"""
        self.assertEqual(subtract(5, 11), 6)
