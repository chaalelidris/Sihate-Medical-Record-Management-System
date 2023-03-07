from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa

from .forms import medicalFileForm
from .models import MedicalFile

# medicalfile/views.


@login_required()
def createPatientMedicalFileView(
    request, template_name="pages/doctor/patient_medical_file.html"
):
    form = medicalFileForm(request.POST or None)

    if form.is_valid():
        patient_medical_file = form.save(commit=False)
        patient_medical_file.save()
        return redirect("patient_list")
    return render(request, template_name, {"form": form})


@login_required()
def updatePatientMedicalFileView(request, id_medical_file):
    # dictionary for initial data with
    # field names as keys
    context = {}

    patient_medical_file = get_object_or_404(
        MedicalFile, id_medical_file=id_medical_file
    )

    form = medicalFileForm(request.POST or None, instance=patient_medical_file)

    if form.is_valid():

        form.save()
        return redirect("patient_list")

    context["form"] = form

    return render(request, "pages/doctor/patient_medical_file.html", context)


@login_required
def deletePatientMedicalFileView(request, id_medical_file):
    # dictionary for initial data with
    # field names as keys
    context = {}

    patient_medical_file = get_object_or_404(
        MedicalFile, id_medical_file=id_medical_file
    )

    if request.method == "POST":

        patient_medical_file.delete()

        return redirect("patient_list")

    return render(request, "pages/doctor/patient_medical_file_delete.html", context)


@login_required()
def fichePDF(request, id_medical_file):
    patient_medical_file = get_object_or_404(
        MedicalFile, id_medical_file=id_medical_file
    )

    template_path = "pages/doctor/fiche_pdf.html"

    context = {"patient_medical_file": patient_medical_file}

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
