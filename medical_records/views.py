from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa

from .forms import medicaRecordForm
from .models import MedicalRecord

# medicalrecord/views.


@login_required()
def createPatientMedicalRecordView(
    request, template_name="profiles/doctor/patient_medical_file.html"
):
    form = medicaRecordForm(request.POST or None)

    if form.is_valid():
        patient_medical_file = form.save(commit=False)
        patient_medical_file.save()
        return redirect("patient_list")
    return render(request, template_name, {"form": form})


@login_required()
def updatePatientMedicalRecordView(request, medicalRecordId):
    # dictionary for initial data with
    # field names as keys
    context = {}

    patient_medical_file = get_object_or_404(
        MedicalRecord, medicalRecordId=medicalRecordId
    )

    form = medicaRecordForm(request.POST or None, instance=patient_medical_file)

    if form.is_valid():

        form.save()
        return redirect("patient_list")

    context["form"] = form

    return render(request, "profiles/doctor/patient_medical_file.html", context)


@login_required
def deletePatientMedicalRecordView(request, medicalRecordId):
    # dictionary for initial data with
    # field names as keys
    context = {}

    patient_medical_file = get_object_or_404(
        MedicalRecord, medicalRecordId=medicalRecordId
    )

    if request.method == "POST":

        patient_medical_file.delete()

        return redirect("patient_list")

    return render(
        request, "profiles/doctor/patient_medical_file_delete.html", context
    )


@login_required()
def medicalRecordPdf(request, medicalRecordId):
    patient_medical_file = get_object_or_404(
        MedicalRecord, medicalRecordId=medicalRecordId
    )

    template_path = "profiles/doctor/fiche_pdf.html"

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
