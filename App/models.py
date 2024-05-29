from django.db import models

# Create your models here.


class Doctor(models.Model):
    full_name = models.CharField(max_length=100)
    mobile_number = models.IntegerField()
    secilization = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.full_name


class Patient(models.Model):
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    mobile_number = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=60)

    def __str__(self):
        return self.full_name


class Appointment(models.Model):
    doctor = models.CharField(max_length=100)
    patient_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.patient_name

    def formatted_date(self):
        return self.date.strftime('%Y-%m-%d') if self.date else ''

    def formatted_time(self):
        return self.time.strftime('%H:%M') if self.time else ''
