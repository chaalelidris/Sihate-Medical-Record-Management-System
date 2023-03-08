from django.urls import path, include
from . import views

# medicalrecord/urls
urlpatterns = [
    path(
        "create_patient_medical_file/",
        views.createPatientMedicalRecordView,
        name="create_patient_medical_file",
    ),
    path(
        "update_patient_medical_file/<int:medicalRecordId>/",
        views.updatePatientMedicalRecordView,
        name="edit_patient_medical_file",
    ),
    path(
        "delete_patient_medical_file/<int:medicalRecordId>/",
        views.deletePatientMedicalRecordView,
        name="delete_patient_medical_file",
    ),
    path(
        "medicalRecordPdf/<int:medicalRecordId>/",
        views.medicalRecordPdf,
        name="medical_record_pdf",
    ),
]
