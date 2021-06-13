from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery.decorators import task

from .calendar import *


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
    print("Updating Events")
    return update_events()
