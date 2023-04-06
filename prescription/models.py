from django.db import models

# prescription/models.


class Prescription(models.Model):
    id_prescription = models.AutoField(primary_key=True)
    patient = models.ForeignKey(
        "medical_records.MedicalRecord",
        related_name="patient_medical_file",
        on_delete=models.CASCADE,
    )
    medication = models.CharField(max_length=254)
    duration = models.IntegerField()
    observation = models.TextField(max_length=254)
    date_prescribed = models.DateTimeField()

    def __str__(self):
        return str(self.date)

    def firstname(self):
        return self.patient.firstname

    def lastname(self):
        return self.patient.lastname

    def age(self):
        return self.patient.age
