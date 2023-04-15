from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .. import forms, models


# ---------------------------------------------------------------------------------------------
# ----------------- OfficeManager views -------------------------------------------------------
# ---------------------------------------------------------------------------------------------


@user_passes_test(lambda u: u.is_authenticated and u.is_manager)
def manager_dashboard_view(request):
    manager = models.OfficeManager.objects.get(id=request.user.id)
    messages.success(request, "Welcome manager")

    context = {
        "manager": manager,
    }
    return render(request, "profiles/manager/dashboard/manager_dashboard.html", context)
