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
    messages.success(request, "Welcome patient ")

    context = {"patient": patient}
    return render(request, "profiles/patient/dashboard/patient_dashboard.html", context)
