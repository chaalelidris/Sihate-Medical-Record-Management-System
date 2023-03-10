from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from django.views.generic.base import TemplateView
from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import redirect, render

from .forms import ContactusForm


# -------------------------------------------------------------------------------
# ------------------------ Home view and Contact Form ---------------------------
# -------------------------------------------------------------------------------


class homeView(TemplateView):
    template_name = "pages/index.html"

    def post(self, request):
        contactForm = ContactusForm()
        if request.method == "POST":
            contactForm = forms.ContactusForm(request.POST)
            if contactForm.is_valid():
                name = contactForm.cleaned_data["Name"]
                email = contactForm.cleaned_data["Email"]
                message = contactForm.cleaned_data["Message"]
                send_mail(
                    str(name) + " || " + str(email),
                    message,
                    settings.EMAIL_HOST_USER,
                    settings.EMAIL_RECEIVING_USER,
                    fail_silently=False,
                )
                return render(request, "hospital/contactussuccess.html")
        return render(request, "hospital/contactus.html", {"form": sub})

        return redirect("index")


# -------------------------------------------------------------------------------
# -------------------------------- User Login  ----------------------------------
# -------------------------------------------------------------------------------
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect("../admin/")

            elif user.is_active:

                if user.is_doctor:
                    login(request, user)
                    return redirect("doctor_view")
                elif user.is_patient:
                    login(request, user)
                    return redirect("patient_view")
                elif user.is_officemanager:
                    login(request, user)
                    return redirect("officemanager_view")
                else:
                    messages.info(request, "User unknown")
                    form = AuthenticationForm()
            else:
                messages.info(request, "User unknown please contact admin !")
                form = AuthenticationForm()
        else:
            messages.info(request, "Username or Password is incorrect")
            form = AuthenticationForm()
    else:
        form = AuthenticationForm()
    return render(request, "pages/login/login.html", {"form": form})


def doctor_signup_view(request):
    if request.method == "POST":
        form = DoctorSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_doctor = True
            user.save()
            doctor = Doctor.objects.create(
                user=user, specialty=form.cleaned_data["specialty"]
            )
            doctor.save()
            return redirect("doctor_view")
    else:
        form = DoctorSignupForm()
    return render(request, "doctor_signup.html", {"form": form})


def patient_signup_view(request):
    if request.method == "POST":
        form = PatientSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_patient = True
            user.save()
            patient = Patient.objects.create(user=user, age=form.cleaned_data["age"])
            patient.save()
            return redirect("patient_view")
    else:
        form = PatientSignupForm()
    return render(request, "patient_signup.html", {"form": form})


def officemanager_signup_view(request):
    if request.method == "POST":
        form = OfficeManagerSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_officemanager = True
            user.save()
            officemanager = OfficeManager.objects.create(
                user=user, phone_number=form.cleaned_data["phone_number"]
            )
            officemanager.save()
            return redirect("officemanager_view")
    else:
        form = OfficeManagerSignupForm()
    return render(request, "officemanager_signup.html", {"form": form})
