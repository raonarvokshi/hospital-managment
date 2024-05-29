from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import auth, User
from .models import Doctor, Patient, Appointment


def redirect_if_authenticated(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, "You are already loged in")
            return redirect("home")
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def redirect_if_not_authenticated(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "You need to log in first")
            return redirect("login")
        return view_func(request, *args, **kwargs)
    return _wrapped_view


@redirect_if_authenticated
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)

        if not username and not password:
            messages.error(request, "Please fill out the required fields!")
            return redirect("login")
        elif not username:
            messages.error(request, "Please enter your first name!")
        elif not password:
            messages.error(request, "Please enter your password!")
            return redirect("login")
        else:
            if user is not None:
                auth.login(request, user)
                messages.success(request, "You logged in successfully!")
                return redirect("home")
            else:
                messages.error(request, "Incorrect credentials!")
                return redirect("login")

    return render(request, "authentication/login.html")


@redirect_if_authenticated
def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists() and User.objects.filter(email=email).exists():
            messages.error(request, "Username and email already exists!")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect("register")

        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect("register")

        else:
            new_user = User.objects.create_user(
                username=username, email=email, password=password)
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.save()
            messages.success(
                request, "Your account was created successfully! please confirm it by logging in")
            return redirect("login")

    return render(request, "authentication/register.html")


def logout(request):
    auth.logout(request)
    messages.success(request, "You logged out successfully!")
    return redirect("login")


def home(request):
    return render(request, "index.html")


@redirect_if_not_authenticated
def doctors(request):
    all_doctors = Doctor.objects.all()
    context = {"doctors": all_doctors}
    return render(request, "doctors/doctors.html", context)


@redirect_if_not_authenticated
def add_doctor(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        phone_number = request.POST.get("phone_number")
        secialization = request.POST.get("secialization")

        new_doctor = Doctor()
        new_doctor.full_name = full_name
        new_doctor.mobile_number = phone_number
        new_doctor.secilization = secialization
        new_doctor.save()
        messages.success(request, "New Doctor Added Successfully!")
        return redirect("doctors")

    return render(request, "doctors/add_doctor.html")


@redirect_if_not_authenticated
def delete_doctor(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    doctor.delete()
    messages.success(request, "Doctor deleted successfully!")
    return redirect("doctors")


@redirect_if_not_authenticated
def edit_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        phone_number = request.POST.get("phone_number")
        secialization = request.POST.get("secialization")

        doctor.full_name = full_name
        doctor.mobile_number = phone_number
        doctor.secilization = secialization
        doctor.save()
        messages.success(request, "Doctor updated successfully!")
        return redirect("doctors")

    return render(request, "doctors/edit_doctor.html", {"doctor": doctor})


@redirect_if_not_authenticated
def patients(request):
    patients = Patient.objects.all()
    context = {"patients": patients}
    return render(request, "patients/patients.html", context)


@redirect_if_not_authenticated
def add_patient(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        gender = request.POST.get("gender")
        mobile_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        address = request.POST.get("address")

        new_patient = Patient()
        new_patient.full_name = full_name
        new_patient.gender = gender
        new_patient.mobile_number = mobile_number
        new_patient.email = email
        new_patient.address = address

        new_patient.save()
        messages.success(request, "New Patient Added Successfully!")
        return redirect("patients")

    return render(request, 'patients/add_patient.html')


@redirect_if_not_authenticated
def edit_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        gender = request.POST.get("gender")
        mobile_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        address = request.POST.get("address")

        patient.full_name = full_name
        patient.gender = gender
        patient.mobile_number = mobile_number
        patient.email = email
        patient.address = address
        patient.save()

        messages.success(request, "Patient Updated successfully!")
        return redirect("patients")

    context = {"patient": patient}
    return render(request, "patients/edit_patient.html", context)


@redirect_if_not_authenticated
def delete_patient(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    patient.delete()
    messages.success(request, "Patient Deleted Successfully!")
    return redirect("patients")


@redirect_if_not_authenticated
def appointments(request):
    appointments = Appointment.objects.all()
    return render(request, "appointments/appointments.html", context={"appointments": appointments})


@redirect_if_not_authenticated
def add_appointment(request):
    doctors = Doctor.objects.all()

    if request.method == "POST":
        doctor = request.POST.get("doctor")
        patient_name = request.POST.get("patient_name")
        date = request.POST.get("date")
        time = request.POST.get("time")

        new_appointment = Appointment()
        new_appointment.doctor = doctor
        new_appointment.patient_name = patient_name
        new_appointment.date = date
        new_appointment.time = time
        new_appointment.save()

        messages.success(request, "New Appointment Added Successfully!")
        return redirect("appointments")
    return render(request, "appointments/add_appointment.html", context={"doctors": doctors})


@redirect_if_not_authenticated
def edit_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    doc = appointment.doctor
    doctors = Doctor.objects.all()
    if request.method == "POST":
        doctor = request.POST.get("doctor")
        patient_name = request.POST.get("patient_name")
        date = request.POST.get("date")
        time = request.POST.get("time")

        appointment.doctor = doctor
        appointment.patient_name = patient_name
        appointment.date = date
        appointment.time = time
        appointment.save()

        messages.success(request, "Appointment Updated Successfully!")
        return redirect("appointments")

    context = {
        "doctors": doctors,
        "appointment": appointment,
        "doc": doc
    }
    return render(request, "appointments/edit_appointment.html", context)


@redirect_if_not_authenticated
def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.delete()
    messages.success(request, "Appointment Deleted Successfully!")
    return redirect("appointments")
