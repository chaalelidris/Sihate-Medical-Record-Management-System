from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.


def medical_office(request):
    if request.user.groups.filter(name="medical_office"):
        return render(request, "pages/medical_office/medical_office_dashboard.html")
    else:
        # messages.info(request, '')
        return redirect("../login")


def medicalOfficeProvileView(request):
    return render(request, "pages/medical_office/medical_office_dashboard.html")
