from django.urls import path, include
from . import views

# medicalfile/urls
urlpatterns = [
    path(
        "create_patient_medical_file/",
        views.createPatientMedicalFileView,
        name="create_patient_medical_file",
    ),
    path(
        "update_patient_medical_file/<int:id_medical_file>/",
        views.updatePatientMedicalFileView,
        name="edit_patient_medical_file",
    ),
    path(
        "delete_patient_medical_file/<int:id_medical_file>/",
        views.deletePatientMedicalFileView,
        name="delete_patient_medical_file",
    ),
    path("fichePDF/<int:id_medical_file>/", views.fichePDF, name="fichePDF"),
]
