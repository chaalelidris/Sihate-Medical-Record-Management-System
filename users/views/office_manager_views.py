from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .. import forms, models


# ---------------------------------------------------------------------------------------------
# ----------------- OfficeManager views -------------------------------------------------------
# ---------------------------------------------------------------------------------------------


@user_passes_test(lambda u: u.is_authenticated and u.is_officemanager)
def manager_dashboard_view(request):
    if request.user.groups.filter(name="office_manager"):
        return render(request, "medical_office/medical_office_dashboard.html")
    else:
        # messages.info(request, '')
        return redirect("login")
