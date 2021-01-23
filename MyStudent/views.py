from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Student, StudentMarkMid2, StudentMarkSem1, StudentMarkMid1, StudentMonthlyAttendance
from MyMentor.models import NotifyStudents, Mentor

# Create your views here.

@login_required
def student_home(request):
    # print(request.user)
    student = Student.objects.filter(studentid=request.user)
    mentor = student.values('mentorname')
#     print(mentor[0]['mentorname'])
    id = Mentor.objects.get(mentorname=mentor[0]['mentorname'])
    notifications = NotifyStudents.objects.all().filter(mentorname=id.id).order_by('-datetime')
#     print(notifications.values())
    context = {
        'students': student.values(),
        'notifications': notifications.values()[:3],
    }
    # print(context['students'])
    return render(request, 'myStudent/home.html', context)


@login_required
def student_mid1(request):
    id = Student.objects.get(studentid=request.user)
#     print(id)
    mid1 = StudentMarkMid1.objects.filter(studentid=id)
#     print(mid1)
    return render(request, 'myStudent/markstable.html', {'marks': mid1, 'value': 0})


@login_required
def student_mid2(request):
    id = Student.objects.get(studentid=request.user)
    mid2 = StudentMarkMid2.objects.filter(studentid=id)
    return render(request, 'myStudent/markstable.html', {'marks': mid2, 'value': 1})


@login_required
def student_sem1(request):
    id = Student.objects.get(studentid=request.user)
    sem1 = StudentMarkSem1.objects.filter(studentid=id)
    return render(request, 'myStudent/markstable.html', {'marks': sem1, 'value': 2})


@login_required
def student_attendance(request):
    id = Student.objects.get(studentid=request.user)
    attendance = StudentMonthlyAttendance.objects.filter(studentid=id)
    return render(request, 'myStudent/attendance.html', {'attendance': attendance})
