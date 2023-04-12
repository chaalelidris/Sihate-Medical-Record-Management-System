from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .. import forms, models
from appointment import models as appointment_models


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
    }
    return render(request, "profiles/doctor/dashboard/doctor_dashboard.html", context)
