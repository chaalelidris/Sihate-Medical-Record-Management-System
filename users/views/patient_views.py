from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .. import forms, models

# ---------------------------------------------------------------------------------------------
# ----------------- Patient views -------------------------------------------------------------
# ---------------------------------------------------------------------------------------------


@user_passes_test(lambda u: u.is_authenticated and u.is_patient)
def patient_dashboard_view(request):
    patient = models.Patient.objects.get(id=request.user.id)
    doctors = models.Doctor.objects.filter(patients__id=request.user.id)
    messages.success(request, "Welcome patient ")

    context = {
        "patient": patient,
        "doctors": doctors,
    }
    return render(request, "profiles/patient/dashboard/patient_dashboard.html", context)


# PROFILE VIEW
@user_passes_test(lambda u: u.is_authenticated and u.is_patient)
def patient_profile_view(request):
    patient = models.Patient.objects.get(id=request.user.id)

    if request.method == "POST":
        form = forms.PatientUpdateForm(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated!")
            return redirect("patient_profile_view")
        else:
            messages.error(
                request, "There was an error updating your profile. Please try again."
            )
    else:
        form = forms.PatientUpdateForm(instance=patient)

    context = {
        "form": form,
        "patient": patient,
    }
    return render(request, "profiles/patient/profile/patient_profile.html", context)
