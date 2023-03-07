from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# medicalfile/models.


class MedicalFile(models.Model):
    SEX_FEMALE = "F"
    SEX_MALE = "M"
    SEX_UNSURE = "U"

    a = "O+"
    b = "O-"
    c = "A+"
    d = "A-"
    e = "B+"
    f = "B-"
    g = "AB+"
    h = "AB-"

    Celebataire = "celebataire"
    Maried = "Maried"
    Divorced = "Divorced"
    Widower = "Widower"

    op = "Oui"
    opp = "Non"

    SEX_OPTIONS = ((SEX_FEMALE, "Female"), (SEX_MALE, "Male"), (SEX_UNSURE, "Unsure"))
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
    SITUATION_OPTIONS = [
        (Celebataire, "Celebataire"),
        (Maried, "Maried"),
        (Divorced, "Divorced"),
        (Widower, "Widower"),
    ]
    OPTIONS = [(op, "Oui"), (opp, "Non")]
    id_medical_file = models.AutoField(primary_key=True)
    id_patient = models.ForeignKey(
        User,
        related_name="patient_medical_file",
        on_delete=models.CASCADE,
    )
    id_doctor = models.ForeignKey(
        User,
        related_name="doctor_medical_file",
        on_delete=models.CASCADE,
    )
    firstname = models.CharField(max_length=254)
    lastname = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    age = models.IntegerField()
    sexe = models.CharField(max_length=1, choices=SEX_OPTIONS, default=None)
    tel = PhoneNumberField(blank=True)
    email = models.EmailField()
    group_sanguin = models.CharField(
        max_length=3, choices=GROUP_SANGUIN_OPTIONS, default=None
    )
    NSS = models.CharField(max_length=254)
    profession = models.CharField(max_length=254)
    motif_consultation = models.CharField(max_length=254)
    establishment_name = models.CharField(max_length=254)
    birthday = models.DateField()
    birthday_location = models.CharField(max_length=254)
    situation = models.CharField(max_length=11, choices=SITUATION_OPTIONS, default=None)
    branch = models.CharField(max_length=254)
    smocking = models.CharField(max_length=3, choices=OPTIONS, default=None)
    general_maladies = models.TextField(max_length=254)
    allergic_reactions_to_drugs = models.TextField(max_length=254)

    def __str__(self):
        return str(self.id_patient.username)
