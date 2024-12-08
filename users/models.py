from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE = (("admin", "Admin"),)
    role = models.CharField(max_length=200, choices=ROLE)
    profile = models.ImageField(upload_to="profile", null=True, blank=True)



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


class Offers(models.Model):
    offers = models.CharField(max_length=300)
    date_time = models.DateTimeField(auto_now=True,editable=False)
    
    def __str__(self):
        return self.offers
