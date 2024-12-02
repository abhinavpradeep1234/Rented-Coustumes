from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE = (("admin", "Admin"),)
    role = models.CharField(max_length=200, choices=ROLE)


class Complaints(models.Model):
    username = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=True, blank=True
    )

    report = models.CharField(max_length=200, null=True, blank=True)
    reported_date = models.DateField(auto_now=True, editable=False)
    respond = models.CharField(max_length=200, null=True, blank=True)


class Notification(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    notification = models.CharField(max_length=200)
    is_read = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)
