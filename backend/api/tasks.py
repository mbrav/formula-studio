from __future__ import print_function
from django.conf import settings
from celery import shared_task

from .calendar import *


@shared_task
def get_cal_events():
    """
    Get events from Google Calendar up from a month ago
    """
    print("Getting Events")
    return get_events()


@shared_task
def create_cal_events():
    """
    Save events in database
    """
    print("Saving Events")
    return create_events()


@shared_task
def update_cal_events():
    """
    Update times events in database
    """
    print("Saving Events")
    return update_events()
