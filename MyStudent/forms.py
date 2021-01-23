from django import forms
from .models import Student, StudentMarkSem1, StudentMarkMid2, StudentMarkMid1, StudentMonthlyAttendance


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        exclude = ['username']


class StudentMarkMid1Form(forms.ModelForm):

    class Meta:
        model = StudentMarkMid1
        fields = '__all__'


class StudentMarkMid2Form(forms.ModelForm):

    class Meta:
        model = StudentMarkMid2
        fields = '__all__'


class StudentMarkSem1Form(forms.ModelForm):

    class Meta:
        model = StudentMarkSem1
        fields = '__all__'


class StudentMonthlyAttendanceForm(forms.ModelForm):

    class Meta:
        model = StudentMonthlyAttendance
        exclude = ['datetime']
