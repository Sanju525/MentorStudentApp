from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Mentor(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    mentorname = models.CharField(max_length=128)
    mentordesignation = models.CharField(max_length=256)


    def __str__(self):
        return self.mentorname


class NotifyStudents(models.Model):
    mentorname = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    message = models.CharField(max_length=256)
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.mentorname)
