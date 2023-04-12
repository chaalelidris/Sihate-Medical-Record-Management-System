from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# medicalRecord/models.


class MedicalRecord(models.Model):

    a = "O+"
    b = "O-"
    c = "A+"
    d = "A-"
    e = "B+"
    f = "B-"
    g = "AB+"
    h = "AB-"

    GROUP_SANGUIN_OPTIONS = [
        (a, "O+"),
        (b, "O-"),
        (c, "A+"),
        (d, "A-"),
        (e, "B+"),
        (f, "B-"),
        (g, "AB+"),
        (h, "AB-"),
    ]

    Celebataire = "celebataire"
    Maried = "Maried"
    Divorced = "Divorced"
    Widower = "Widower"

    SITUATION_OPTIONS = [
        (Celebataire, "Celebataire"),
        (Maried, "Maried"),
        (Divorced, "Divorced"),
        (Widower, "Widower"),
    ]

    Yes = "Oui"
    No = "Non"

    OPTIONS = [(Yes, "Yes"), (No, "NO")]

    patient = models.ForeignKey(
        "users.Patient",
        related_name="patient_medical_file",
        on_delete=models.CASCADE,
    )
    doctor = models.ForeignKey(
        "users.Doctor",
        related_name="doctor_medical_file",
        on_delete=models.CASCADE,
    )
    group_sanguin = models.CharField(
        max_length=3, choices=GROUP_SANGUIN_OPTIONS, default=None
    )
    NSS = models.CharField(max_length=254)
    profession = models.CharField(max_length=254)
    establishment_name = models.CharField(max_length=254)
    birthday = models.DateField()
    birthday_location = models.CharField(max_length=254)
    situation = models.CharField(max_length=11, choices=SITUATION_OPTIONS, default=None)
    smocking = models.CharField(max_length=3, choices=OPTIONS, default=None)
    general_maladies = models.TextField(max_length=254)
    allergic_reactions_to_drugs = models.TextField(max_length=254)

    def __str__(self):
        return str(self.patient_id.username)


# ---------------------------------------------------------------------------------------------
# ------------------------------------- Prescription Model -----------------------------------
# ---------------------------------------------------------------------------------------------
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
