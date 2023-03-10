from django.contrib.auth.models import AbstractUser
from django.db import models

# ----------------Import PhoneNumberField ------------------
from phonenumber_field.modelfields import PhoneNumberField

# ----------------------------------------------------------------------------
# ---------------------------- User models -----------------------------------
# ----------------------------------------------------------------------------
class User(AbstractUser):
    pass


# ----------------------------------------------------------------------------
# ---------------------------- Doctor models ---------------------------------
# ----------------------------------------------------------------------------


class Doctor(User):
    departments = [
        ("Cardiologist", "Cardiologist"),
        ("Generalist", "Generalist"),
        ("Dermatologists", "Dermatologists"),
        ("Emergency Medicine Specialists", "Emergency Medicine Specialists"),
        ("Allergists/Immunologists", "Allergists/Immunologists"),
        ("Anesthesiologists", "Anesthesiologists"),
        ("Colon and Rectal Surgeons", "Colon and Rectal Surgeons"),
    ]

    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)
    department = models.CharField(
        max_length=50, choices=departments, default="Generalist"
    )
    profile_pic = models.ImageField(
        upload_to="profile_pic/DoctorProfilePic/", null=True, blank=True
    )
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"

    def __str__(self):
        return "{} ({})".format(self.first_name, self.department)

    @property
    def get_name(self):
        return self.first_name + " " + self.last_name

    @property
    def get_id(self):
        return self.id

    @property
    def is_doctor(self):
        return True


# --------------------------------------------------------------------------------------------
# --------------------------------------- Patient models -------------------------------------
# --------------------------------------------------------------------------------------------


class Patient(User):

    assigned_doctor_id = models.PositiveIntegerField(null=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)
    symptoms = models.CharField(max_length=100, null=False)
    admit_date = models.DateField(auto_now=True)
    profile_pic = models.ImageField(
        upload_to="profile_pic/PatientProfilePic/", null=True, blank=True
    )
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"

    @property
    def get_name(self):
        return self.first_name + " " + self.last_name

    @property
    def get_id(self):
        return self.id

    def __str__(self):
        return self.first_name + " (" + self.symptoms + ")"

    @property
    def is_patient(self):
        return True


# ---------------------------------------------------------------------------------------------
# ------------------------------------- Office Manager Models -----------------------------------
# ---------------------------------------------------------------------------------------------


class OfficeManager(User):
    name = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    mobile = PhoneNumberField(blank=True)
    profile_pic = models.ImageField(
        upload_to="profile_pic/OfficeManagerProfilePic/", null=True, blank=True
    )

    class Meta:
        verbose_name = "OfficeManager"
        verbose_name_plural = "OfficeManagers"

    def __str__(self):
        return str(self.name)

    @property
    def is_officemanager(self):
        return True


# ---------------------------------------------------------------------------------------------
# ------------------------------------- consultation Models -----------------------------------
# ---------------------------------------------------------------------------------------------


class Consultation(models.Model):
    doctorId = models.ForeignKey(
        "users.Doctor",
        related_name="conssultation_doctor",
        on_delete=models.CASCADE,
    )
    patientId = models.ForeignKey(
        "users.Patient",
        related_name="consultation_patient",
        on_delete=models.CASCADE,
    )
    consultationDate = models.DateTimeField()
    notes = models.TextField(max_length=254)
    diagnosis = models.TextField()
    treatment = models.TextField()

    def __str__(self):
        return str(self.patientId.username)
