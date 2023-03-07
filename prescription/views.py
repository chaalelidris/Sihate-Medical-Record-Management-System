from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa

from .models import Prescription
from .forms import PrescriptionForm

# Prescription/views .


@login_required()
def prescription_pdf(request, id_ordonnance):
    ordonnance = get_object_or_404(Prescription, id_ordonnance=id_ordonnance)

    template_path = "pages/doctor/pdf_template.html"

    context = {"ordonnance": ordonnance}

    response = HttpResponse(content_type="application/pdf")

    response["Content-Disposition"] = 'filename="ordonnance.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse("We had some errors <pre>" + html + "</pre>")
    return response


def PrescriptionListView(request):
    prescription = Prescription.objects.all()
    return render(
        request,
        "pages/doctor/prescription/prescription_list.html",
        {"prescription": prescription},
    )


def PrescriptionCreateView(
    request, template_name="pages/doctor/prescription/prescription.html"
):
    form = PrescriptionForm(request.POST or None)

    if form.is_valid():
        prescription = form.save(commit=False)
        prescription.save()
        return redirect("prescription_list")
    return render(request, template_name, {"form": form})


def PrescriptionUpdateView(request, id_prescription):
    # dictionary for initial data with
    # field names as keys
    context = {}

    prescription = get_object_or_404(Prescription, id_prescription=id_prescription)

    form = PrescriptionForm(request.POST or None, instance=prescription)

    if form.is_valid():

        form.save()
        return redirect("prescription_list")

    context["form"] = form

    return render(request, "pages/doctor/prescription/prescription.html", context)


@login_required
def PrescriptionDeleteView(request, id_prescription):
    # dictionary for initial data with
    # field names as keys
    context = {}

    prescription = get_object_or_404(Prescription, id_prescription=id_prescription)

    if request.method == "POST":

        prescription.delete()

        return redirect("prescription_list")

    return render(
        request, "pages/doctor/prescription/delete_prescription.html", context
    )
