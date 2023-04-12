
from django.contrib import messages

from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import redirect, render

from .forms import ContactusForm

# -------------------------------------------------------------------------------
# -------------for checking user is doctor , patient or admin(by sumit)----------
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# ------------------------ Home view and Contact Form ---------------------------
# -------------------------------------------------------------------------------
def home_view(request):
    return render(request, "index/index.html")
