from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    def __str__(self):
        return self.username


# ----------------------------------------------------------------------------
# ---------------------------- Doctor models ---------------------------------
# ----------------------------------------------------------------------------

departments = [
    ("Cardiologist", "Cardiologist"),
    ("Generalist", "Generalist"),
    ("Dermatologists", "Dermatologists"),
    ("Emergency Medicine Specialists", "Emergency Medicine Specialists"),
    ("Allergists/Immunologists", "Allergists/Immunologists"),
    ("Anesthesiologists", "Anesthesiologists"),
    ("Colon and Rectal Surgeons", "Colon and Rectal Surgeons"),
]


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to="profile_pic/DoctorProfilePic/", null=True, blank=True
    )
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)
    department = models.CharField(
        max_length=50, choices=departments, default="Generalist"
    )
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return "{} ({})".format(self.user.first_name, self.department)


# --------------------------------------------------------------------------------------------
# --------------------------------------- Patient models -------------------------------------
# --------------------------------------------------------------------------------------------


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to="profile_pic/PatientProfilePic/", null=True, blank=True
    )
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)
    symptoms = models.CharField(max_length=100, null=False)
    assignedDoctorId = models.PositiveIntegerField(null=True)
    admitDate = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name + " (" + self.symptoms + ")"


# ---------------------------------------------------------------------------------------------
# ------------------------------------- Office Admin Models -----------------------------------
# ---------------------------------------------------------------------------------------------


class MedicalOffice(models.Model):
    Name = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    email = models.EmailField()
    tel = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)

    def __str__(self):
        return str(self.Name)


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
