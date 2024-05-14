import datetime
from celery import shared_task
from django.conf import settings
from courses.models import Course, Sub
from django.core.mail import send_mail

from users.models import User


@shared_task
def check_updates(pk: int, date: datetime.datetime):
    instance = Course.objects.filter(id=pk).first()
    if instance:
        hour_delta = (instance.last_update - date).total_seconds() / 3600
        if hour_delta < 4:
            subs = Sub.objects.filter(course=instance)
            if len(list(subs)) > 0:
                subscribers = []
                for sub in subs:
                    subscribers.append(User.objects.get(id=sub.user.id).email)
                response = send_mail(
                    subject=f"Курс {instance.name} обновился!!!",
                    message=f"Курс {instance.name} получил обновления, посмотрите, что там!!!",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=subscribers,
                    fail_silently=False,
                )
                print(response)


@shared_task
def check_login():
    users = User.objects.filter(is_active=True)
    if users.exists():
        for user in users:
            print("go")
            if datetime.datetime.now() - user.last_login > datetime.timedelta(weeks=4):
                user.is_active = False
                user.save()
