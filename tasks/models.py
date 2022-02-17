from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete


STATUS_CHOICES = (
    ("PENDING", "PENDING"),
    ("IN_PROGRESS", "IN_PROGRESS"),
    ("COMPLETED", "COMPLETED"),
    ("CANCELLED", "CANCELLED"),
)


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        choices=STATUS_CHOICES, max_length=100, default=STATUS_CHOICES[0][0]
    )
    created_date = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    mail_time = models.TimeField(blank=True, null=True, editable=True)

    def __str__(self):
        return f"Profile: {self.user}" if self.user else "Profile: Anonymous"


@receiver(post_save, sender=User)
def create_mail(sender, **kwargs):
    new_profile = UserProfile()
    new_profile.save()
