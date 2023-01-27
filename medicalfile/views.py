from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa

from .forms import medicalFileForm
from .models import MedicalFile

# medicalfile/views.


@login_required()
def fiche_patient(request, template_name="pages/doctor/fiche_patient.html"):
    form = medicalFileForm(request.POST or None)

    if form.is_valid():
        fiche_patient = form.save(commit=False)
        fiche_patient.save()
        return redirect("patient_list")
    return render(request, template_name, {"form": form})


@login_required()
def fiche_patient_edit(request, id_fiche):
    # dictionary for initial data with
    # field names as keys
    context = {}

    fiche_patient = get_object_or_404(MedicalFile, id_fiche=id_fiche)

    form = medicalFileForm(request.POST or None, instance=fiche_patient)

    if form.is_valid():

        form.save()
        return redirect("patient_list")

    context["form"] = form

    return render(request, "pages/doctor/fiche_patient.html", context)


@login_required
def fiche_patient_delete(request, id_fiche):
    # dictionary for initial data with
    # field names as keys
    context = {}

    fiche_patient = get_object_or_404(MedicalFile, id_fiche=id_fiche)

    if request.method == "POST":

        fiche_patient.delete()

        return redirect("patient_list")

    return render(request, "pages/doctor/fiche_patient_delete.html", context)


@login_required()
def fichePDF(request, id_fiche):
    fiche_patient = get_object_or_404(MedicalFile, id_fiche=id_fiche)

    template_path = "pages/doctor/fiche_pdf.html"

    context = {"fiche_patient": fiche_patient}

    response = HttpResponse(content_type="application/pdf")

    response["Content-Disposition"] = 'filename="dossier medicale de patient.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse("We had some errors <pre>" + html + "</pre>")
    return response
