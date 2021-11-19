import os
from datetime import datetime, timedelta
from pathlib import Path

import pytz
from django.conf import settings
from django.core.management.base import BaseCommand
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from formula_studio.models import EventCategory, Instructor, ScheduleEvent

local_timezone = pytz.timezone(settings.TIME_ZONE)
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

# Find the project base directory
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_PATH = os.path.abspath(__file__)
# Specify number of directories to go up from current file
PATH_UP = 3
BASE_DIR = str(Path(FILE_PATH).parents[PATH_UP])
auth_path = '/App/management/commands/auth/'
data_path = '/App/management/commands/data/'


def get_events():
    """
    Get events from Google Calendar up from a month ago
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(BASE_DIR + auth_path + 'token.json'):
        creds = Credentials.from_authorized_user_file(
            BASE_DIR + auth_path + 'token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                BASE_DIR + auth_path + 'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(BASE_DIR + auth_path + 'token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.now() - timedelta(days=30)
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


def save_events_to_file():
    events = get_events()
    file = open(BASE_DIR + data_path + 'event-list.csv', 'w')
    for event in events:
        id = event['id']
        start = event['start'].get('dateTime', event['start'].get('date'))
        file.write(id + ", " + str(start) + ", " +
                   str(event['summary']) + "\n")
    file.close()


def create_events():
    events = get_events()
    instruct = Instructor.objects.get(pk=2)
    event_category = EventCategory.objects.get(pk=1)

    created_events = 0
    for event in events:
        id = event['id']
        if not ScheduleEvent.objects.filter(google_cal_id=id):
            event_date = event['start'].get('dateTime')
            print("Event does not exist, creating: ",
                  event['summary'], event_date)
            new_event = ScheduleEvent(
                google_cal_id=id,
                name=event['summary'],
                date=event_date,
                category=event_category,
                instructor=instruct
            )
            new_event.save()
            created_events += 1
    msg = 'Created' + str(create_events) + 'events.'
    return(msg)


def update_events():
    events = get_events()
    updated_events = 0
    for event in events:
        id = event['id']
        event_db = ScheduleEvent.objects.get(google_cal_id=id)
        event_date = datetime.fromisoformat(
            event['start'].get('dateTime', event['start'].get('date')))

        # Django stores dates in UTC when USE_TZ = True in settings
        # Hence conversion is necessary, but when saving, Django handles things automatically
        # https://stackoverflow.com/a/14714819
        event_db_local_date = event_db.date.replace(
            tzinfo=pytz.utc).astimezone(local_timezone)

        if event_db_local_date != event_date:
            print("Event time change, updating",
                  event_db_local_date, "to", event_date)
            event_db.date = event_date
            event_db.save()

        if event_db.name != event['summary']:
            print("Event name change, updating",
                  event_db.name, "to", event['summary'])
            event_db.name = event['summary']
            event_db.save()
    msg = 'Updated ' + str(updated_events) + ' events.'
    return(msg)


class Command(BaseCommand):
    """Google Cal Command"""

    def add_arguments(self, parser):
        """Optional arguments"""
        parser.add_argument('-g', '--get', action='store_true',
                            help='Get Events and create Google auth creds if necessary', )
        parser.add_argument('-s', '--save', action='store_true',
                            help='Save Events to file', )
        parser.add_argument('-c', '--create', action='store_true',
                            help='Create Events in db', )
        parser.add_argument('-u', '--update', action='store_true',
                            help='Update Events in db', )

    def handle(self, *args, **kwargs):
        """Handle the command"""

        get = kwargs['get']
        save = kwargs['save']
        create = kwargs['create']
        update = kwargs['update']
        if get:
            get_events()
        if save:
            save_events_to_file()
        if create:
            create_events()
        if update:
            update_events()

        if (get or save or create or update) is not True:
            create_events()
            update_events()
