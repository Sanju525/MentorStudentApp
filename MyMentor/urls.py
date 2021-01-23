"""MyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views as mentorViews
urlpatterns = [
    path('login/', mentorViews.mentor_login, name='mentorLogin'),
    path('logout/', mentorViews.mentor_logout, name='mentorLogout'),
    path('home/', mentorViews.mentor_home, name='mentorHome'),
    path('notify-students/', mentorViews.notify_student, name='NotifyStudent'),
    path('studentregistrations/', mentorViews.register_student, name='registerStudent'),
    path('enter-student-marks-mid1/', mentorViews.enter_mid1, name='StudentMid1'),
    path('enter-student-marks-mid2/', mentorViews.enter_mid2, name='StudentMid2'),
    path('enter-student-marks-sem1/', mentorViews.enter_sem1, name='StudentSem1'),
    path('enter-student-attendance/', mentorViews.student_monthly_attendance, name='Attendance'),
]
