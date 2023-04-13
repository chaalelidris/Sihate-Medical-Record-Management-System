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


@user_passes_test(lambda u: u.is_authenticated and u.is_doctor)
def doctor_profile_view(request):
    doctor = models.Doctor.objects.get(id=request.user.id)

    if request.method == "POST":
        form = forms.DoctorUpdateForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
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
    }
    return render(request, "profiles/doctor/profile/doctor_profile.html", context)
