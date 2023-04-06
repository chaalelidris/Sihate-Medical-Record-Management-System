from django.contrib.auth.models import AbstractUser
from django.db import models

# ----------------Import PhoneNumberField ------------------
from phonenumber_field.modelfields import PhoneNumberField

# ----------------------------------------------------------------------------
# ---------------------------- User models -----------------------------------
# ----------------------------------------------------------------------------
class User(AbstractUser):
    is_doctor = models.BooleanField("doctor status", default=False)
    is_patient = models.BooleanField("patient status", default=False)
    is_office_manager = models.BooleanField("office manager status", default=False)


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
    patients = models.ManyToManyField("Patient", related_name="doctors")
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


# --------------------------------------------------------------------------------------------
# --------------------------------------- Patient models -------------------------------------
# --------------------------------------------------------------------------------------------


class Patient(User):

    SEX_FEMALE = "F"
    SEX_MALE = "M"
    SEX_UNSURE = "U"

    SEX_OPTIONS = ((SEX_FEMALE, "Female"), (SEX_MALE, "Male"))

    age = models.IntegerField(default=None)
    sexe = models.CharField(max_length=1, choices=SEX_OPTIONS, default=None)
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


# ---------------------------------------------------------------------------------------------
# ------------------------------------- consultation Models -----------------------------------
# ---------------------------------------------------------------------------------------------


class Consultation(models.Model):
    appointment = models.ForeignKey(
        "appointment.Appointment",
        related_name="appointments",
        on_delete=models.CASCADE,
        default="",
    )
    consultation_date = models.DateTimeField()
    notes = models.TextField(max_length=254)
    diagnosis = models.TextField()
    treatment = models.TextField()

    def __str__(self):
        return str(self.patient_id.username)
