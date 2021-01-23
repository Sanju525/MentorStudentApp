from django.db import models
from MyMentor.models import Mentor
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Student(models.Model):
    username = models.ManyToManyField(User)
    studentid = models.CharField(max_length=10, unique=True, primary_key=True)
    name = models.CharField(max_length=128)
    sem = models.IntegerField()
    branch = models.CharField(max_length=128)
    batch = models.IntegerField()
    regulation = models.CharField(max_length=32)
    mentorname = models.CharField(max_length=64)

    def __str__(self):
        return str(self.studentid)

    def get_studentid(self):
        return str(self.studentid)


class StudentMarkMid1(models.Model):
    studentid = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject0 = models.IntegerField()
    subject1 = models.IntegerField()
    subject2 = models.IntegerField()
    subject3 = models.IntegerField()
    subject4 = models.IntegerField()
    subject5 = models.IntegerField()
    subject6 = models.IntegerField()
    lab0 = models.IntegerField()
    lab1 = models.IntegerField()


    def __str__(self):
        return str(self.studentid)



class StudentMarkMid2(models.Model):
    studentid = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject0 = models.IntegerField()
    subject1 = models.IntegerField()
    subject2 = models.IntegerField()
    subject3 = models.IntegerField()
    subject4 = models.IntegerField()
    subject5 = models.IntegerField()
    subject6 = models.IntegerField()
    lab0 = models.IntegerField()
    lab1 = models.IntegerField()


    def __str__(self):
        return str(self.studentid)


class StudentMarkSem1(models.Model):
    studentid = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject0 = models.IntegerField()
    subject1 = models.IntegerField()
    subject2 = models.IntegerField()
    subject3 = models.IntegerField()
    subject4 = models.IntegerField()
    subject5 = models.IntegerField()
    subject6 = models.IntegerField()
    lab0 = models.IntegerField()
    lab1 = models.IntegerField()
    sgpa = models.FloatField()
    cgpa = models.FloatField()

    def __str__(self):
        return str(self.studentid)


class StudentMonthlyAttendance(models.Model):
    studentid = models.ForeignKey(Student, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now)
    percentage = models.FloatField()