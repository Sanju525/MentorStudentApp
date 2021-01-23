from django.contrib import admin
from .models import Student, StudentMarkMid1, StudentMarkMid2, StudentMarkSem1

# Register your models here.

admin.site.register(Student)
admin.site.register(StudentMarkMid1)
admin.site.register(StudentMarkMid2)
admin.site.register(StudentMarkSem1)
