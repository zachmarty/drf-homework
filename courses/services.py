import datetime
import json
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import pytz


schedule, created = IntervalSchedule.objects.get_or_create(
    every=10, period=IntervalSchedule.SECONDS
)

PeriodicTask.objects.create(
    interval=schedule,
    name="Check last login",
    task="proj.tasks.check_login",
    expires=datetime.datetime.now(pytz.timezone("Europe/Moscow"))
    + datetime.timedelta(seconds=30),
)
