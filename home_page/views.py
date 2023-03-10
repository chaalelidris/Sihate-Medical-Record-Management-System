from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import ContactusForm
from users import forms as users_forms


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
        form = users_forms.DoctorSignupForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"Account created for {user.username}!")
            return redirect("doctor_view")
    else:
        form = users_forms.DoctorSignupForm()
    return render(request, "pages/register/doctor_signup.html", {"form": form})


def patient_signup_view(request):
    if request.method == "POST":
        form = users_forms.PatientSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"Account created for {user.username}!")
            return redirect("patient_view")
    else:
        form = users_forms.PatientSignupForm()
    return render(request, "pages/register/patient_signup.html", {"form": form})


def officemanager_signup_view(request):
    if request.method == "POST":
        form = users_forms.OfficeManagerSignupForm(request.POST, request.FILES)
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
        form = users_forms.OfficeManagerSignupForm()
    return render(request, "pages\register\officemanager_signup.html", {"form": form})
