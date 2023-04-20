from django.contrib import messages

from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import redirect, render

from .forms import ContactusForm
from users import models as users_modals

# -------------------------------------------------------------------------------
# -------------for checking user is doctor , patient or admin(by sumit)----------
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# ------------------------ Home view and Contact Form ---------------------------
# -------------------------------------------------------------------------------
def home_view(request):
    doctors = users_modals.Doctor.objects.order_by("-id")[:4]
    context = {
        "doctors": doctors,
    }
    return render(request, "index/index.html", context)
