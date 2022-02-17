from tasks.models import Task, UserProfile
from datetime import datetime, timedelta
import time

from django.contrib.auth.models import User
from django.core.mail import send_mail

from celery.decorators import periodic_task

from task_manager.celery import app


class Mailer:
    def __init__(self):
        self.recipients = User.objects.values()
        self.recipients_count = self.recipients.count()
        self.mailer_index = 0
        self.user_index = 0

    def get_email(self):
        if self.mailer_index < self.recipients_count:
            yield self.recipients[self.mailer_index]["email"]
            self.mailer_index += 1

    def email_content(self):
        if self.user_index < self.recipients_count:
            return f"Hello {self.recipients[self.mailer_index]['username']}! You have {Task.objects.filter(user=self.recipients[self.mailer_index]['id']).exclude(status='COMPLETED').count()} tasks pending"

    def reset(self):
        self.mailer_index = 0
        self.user_index = 0


mailer = Mailer()


@periodic_task(run_every=timedelta(seconds=15))
def send_email_reminder():
    print("Starting to process email")

    for address in mailer.get_email():
        content = mailer.email_content()
        send_mail("Task Manager - Notifications", content, "admin@admin.com", [address])

    print("\n\nCompleted sending mails\n\n")
    mailer.reset()


@app.task
def test_background_jobs():
    print("This is from the bg")
    for i in range(10):
        time.sleep(1)
        print(i)

@app.task
def mail_user(user: User):
    address = user.email
    content = f"Hello {self.recipients[self.mailer_index]['username']}! You have {Task.objects.filter(user=self.recipients[self.mailer_index]['id']).exclude(status='COMPLETED').count()} tasks pending"
    send_mail("Task Manager - Notifications", content, "admin@admin.com", [address])
    
@app.task
def monitor_mail_times():
    