from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .. import forms, models
from appointment import models as appointment_models
from medical_records import models as medical_records_models


# ---------------------------------------------------------------------------------------------
# --------------------------------------- Doctor views ----------------------------------------
# ---------------------------------------------------------------------------------------------


@user_passes_test(lambda u: u.is_authenticated and u.is_doctor)
def doctor_dashboard_view(request):
    doctor = models.Doctor.objects.get(id=request.user.id)
    appointments = appointment_models.Appointment.objects.filter(doctor=doctor)
    patients = doctor.patients.all()
    messages.success(request, "Welcome doctor ")

    context = {
        "doctor": doctor,
        "appointments": appointments,
        "patients": patients,
        "segment": "dashboard",
    }
    return render(request, "profiles/doctor/dashboard/doctor_dashboard.html", context)


@user_passes_test(lambda u: u.is_authenticated and u.is_doctor)
def doctor_profile_view(request):
    doctor = models.Doctor.objects.get(id=request.user.id)

    if request.method == "POST":
        form = forms.DoctorUpdateForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            # Delete old profile pic if it exists
            if doctor.profile_pic:
                doctor.profile_pic.delete()

            form.save()
            messages.success(request, "Your profile has been updated!")
            return redirect("doctor_profile_view")
        else:
            messages.error(
                request, "There was an error updating your profile. Please try again."
            )
    else:
        form = forms.DoctorUpdateForm(instance=doctor)

    context = {
        "form": form,
        "doctor": doctor,
        "segment": "profile",
    }
    return render(request, "profiles/doctor/profile/doctor_profile.html", context)


@user_passes_test(lambda u: u.is_authenticated and u.is_doctor)
def doctor_patients_view(request):
    doctor = models.Doctor.objects.get(id=request.user.id)
    patients = doctor.patients.all()
    context = {
        "doctor": doctor,
        "patients": patients,
        "segment": "patients",
    }
    return render(request, "profiles/doctor/patients/patients.html", context)


@user_passes_test(lambda u: u.is_authenticated and u.is_doctor)
def doctor_records_view(request):
    doctor = models.Doctor.objects.get(id=request.user.id)
    records = medical_records_models.MedicalRecord.objects.filter(doctor=request.user)

    context = {
        "records": records,
        "doctor": doctor,
        "segment": "records",
    }
    return render(request, "profiles/doctor/records/doctor_records.html", context)


@user_passes_test(lambda u: u.is_authenticated and u.is_doctor)
def doctor_appointments_view(request):
    doctor = models.Doctor.objects.get(id=request.user.id)
    appointments = appointment_models.Appointment.objects.filter(doctor=request.user)

    context = {
        "appointments": appointments,
        "doctor": doctor,
        "segment": "appointments",
    }
    return render(
        request, "profiles/doctor/appointments/doctor_appointments.html", context
    )
