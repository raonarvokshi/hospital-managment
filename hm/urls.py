"""
URL configuration for hm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout, name="logout"),
    path("doctors/", doctors, name="doctors"),
    path("add-doctor/", add_doctor, name="add_doctor"),
    path("delete-doctor/<str:doctor_id>/", delete_doctor, name="delete_doctor"),
    path("edit-doctor/<str:doctor_id>/", edit_doctor, name="edit_doctor"),
    path("patients/", patients, name="patients"),
    path("add-patient/", add_patient, name="add_patient"),
    path("edit-patient/<str:patient_id>/", edit_patient, name="edit_patient"),
    path("delete-patient/<str:patient_id>/",
         delete_patient, name="delete_patient"),
    path("appointments/", appointments, name="appointments"),
    path("add-appointment/", add_appointment, name="add_appointment"),
    path("edit-appointment/<str:appointment_id>/",
         edit_appointment, name="edit_appointment"),
    path("delete-appointment/<str:appointment_id>/",
         delete_appointment, name="delete_appointment")
]
