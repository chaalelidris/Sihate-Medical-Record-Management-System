from django.urls import path, include
from .views import (
    PrescriptionListView,
    PrescriptionCreateView,
    PrescriptionUpdateView,
    PrescriptionDeleteView,
    prescription_pdf,
)

urlpatterns = [
    path("", PrescriptionCreateView, name="prescription"),
    path("prescription_list/", PrescriptionListView, name="prescription_list"),
    path(
        "prescription_update/<int:id_ordonnance>/",
        PrescriptionUpdateView,
        name="prescription_update",
    ),
    path(
        "prescription_delete/<int:id_ordonnance>/",
        PrescriptionDeleteView,
        name="prescription_delete",
    ),
    path(
        "prescription_pdf/<int:id_ordonnance>/",
        prescription_pdf,
        name="prescription_pdf",
    ),
]
