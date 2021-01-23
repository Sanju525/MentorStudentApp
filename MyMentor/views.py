from django.shortcuts import render
from django.contrib.auth.models import User

# Packages For Mentor Login
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

#
from MyStudent.models import Student, StudentMonthlyAttendance
from .models import Mentor, NotifyStudents


# Student Forms
from MyStudent.forms import StudentForm, StudentMarkMid1Form, StudentMarkMid2Form,\
    StudentMarkSem1Form, StudentMonthlyAttendanceForm

# Create your Mentor views here.


# For login view
def mentor_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        request.session['presentuser'] = username
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active and user.is_staff:
                request.session['isMentor'] = True
                login(request, user)
                return HttpResponseRedirect(reverse('mentorHome'))
            else:
                return HttpResponse("YOU ARE NOT A STAFF MEMBER. <a href='/'>Go Home</a>")
        else:
            print("Student Tried to login or login failed")
            print("username {} and password {}".format(username, password))
            return HttpResponse("INVALID DETAILS <a href='/'>Go Home</a>")
    else:
        return render(request, 'myMentor/login.html')


@login_required
def mentor_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('HomePage'))


# Consists CRUD student, students marks, student attendance, notifications.
@login_required
def mentor_home(request):
    if request.session.get('isMentor'):
        username = request.session.get('presentuser')
        # Get Mentor ID to Get Mentor UserName
        mentorUser = User.objects.filter(username=username).values('id')
        mentorUserDict = mentorUser[0]
        mentorid = mentorUserDict['id']

        # Get MentorName to get the students under Mentor
        mentor = Mentor.objects.filter(username=mentorid).values('mentorname')
        print(mentor)
        mentorDict = mentor[0]
        mentorname = mentorDict['mentorname']
        print(mentorname)
        request.session['mentorname'] = mentorname
        print(request.session.get('mentorname'))
        # Get Students by using mentorName

        students = Student.objects.filter(mentorname=mentorname)

        # students = Student.objects.filter(mentorname=mentor)
        return render(request, 'myMentor/home.html', {'students': students})
    else:
        return HttpResponse("404 Page not found.")


@login_required
def register_student(request):
    if request.session.get('isMentor'):
        if request.method == 'POST':
            form = StudentForm(request.POST)
            if form.is_valid():
                # Create account for students
                student_username = request.POST.get('studentid')
                # print(student_username)
                User.objects.create_user(username=student_username, password='tkrcet@123')
                form.save(commit=False)
                form.username = request.user
                form.save()
                return HttpResponseRedirect(reverse('registerStudent'))
        else:
            form = StudentForm()
            return render(request, 'MyMentor/studentreg.html', {'form': form, 'mentorname': request.session.get('mentorname')})
    else:
        return HttpResponse("404 page not found.")


@login_required
def enter_mid1(request):
    if request.session.get('isMentor'):
        if request.method == 'POST':
            form = StudentMarkMid1Form(request.POST)
            form.save()
            return HttpResponseRedirect(reverse('StudentMid1'))
        else:
            form = StudentMarkMid1Form()
            return render(request, 'MyMentor/marksdetails.html', {'form': form, 'value': 1})
    else:
        return HttpResponse("404 Page not found.")
    
    
@login_required
def enter_mid2(request):
    if request.session.get('isMentor'):
        if request.method == 'POST':
            form = StudentMarkMid2Form(request.POST)
            form.save()
            return HttpResponseRedirect(reverse('StudentMid2'))
        else:
            form = StudentMarkMid2Form()
            return render(request, 'MyMentor/marksdetails.html', {'form': form, 'value': 2})
    else:
        return HttpResponse("404 page not found.")
    
    
@login_required
def enter_sem1(request):
    if request.session.get('isMentor'):
        if request.method == 'POST':
            form = StudentMarkSem1Form(request.POST)
            form.save()
            return HttpResponseRedirect(reverse('StudentSem1'))
        else:
            form = StudentMarkSem1Form()
            return render(request, 'MyMentor/marksdetails.html', {'form': form, 'value': 3})
    else:
        return HttpResponse("404 page not found.")


@login_required
def notify_student(request):
    if request.session.get('isMentor'):
        if request.method == 'POST':
            message = request.POST.get('message')
            MentorUSer = User.objects.get(username=request.session.get('presentuser'))
            id = Mentor.objects.get(username=MentorUSer.id)
            # print(id.id)
            NotifyStudents.objects.create(mentorname=id, message=message)
            return HttpResponseRedirect(reverse('NotifyStudent'))
        else:
            MentorUSer = User.objects.get(username=request.session.get('presentuser'))
            id = Mentor.objects.get(username=MentorUSer.id)
            notifications = NotifyStudents.objects.all().filter(mentorname=id).order_by('-datetime')
            print(notifications)
            return render(request, 'MyMentor/notifystudents.html', {'notifications': notifications})
    else:
        return HttpResponse("404 page not found.")


@login_required
def student_monthly_attendance(request):
    if request.session.get('isMentor'):
        if request.method == 'POST':
            form = StudentMonthlyAttendanceForm(request.POST)
            form.save()
            return HttpResponseRedirect(reverse('Attendance'))
        else:
            form = StudentMonthlyAttendanceForm()
            return render(request, 'MyMentor/marksdetails.html', {'form': form, 'value': 4})
    else:
        return HttpResponse("404 page not found.")
