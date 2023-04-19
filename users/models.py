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
    is_manager = models.BooleanField("office manager status", default=False)


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
    patients = models.ManyToManyField("users.Patient", related_name="patients")
    address = models.CharField(max_length=40, blank=True, default="/")
    mobile = models.CharField(max_length=20, null=True)
    department = models.CharField(
        max_length=50, choices=departments, default="Generalist"
    )
    admit_date = models.DateField(auto_now=True)
    profile_pic = models.ImageField(
        upload_to="profile_pic/DoctorProfilePic/", null=True, blank=True
    )
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"

    def __str__(self):
        return "{} ({})".format(self.username, self.department)

    @property
    def get_name(self):
        return self.first_name + " " + self.last_name

    @property
    def get_id(self):
        return self.id

    @property
    def get_status(self):
        return "Approved" if self.status else "Pending"

    @property
    def get_profile_pic(self):
        if self.profile_pic:
            return self.profile_pic.url
        else:
            return "/static/assets/profile/img/default/default_profile_picture.png"


# --------------------------------------------------------------------------------------------
# --------------------------------------- Patient models -------------------------------------
# --------------------------------------------------------------------------------------------


class Patient(User):
    GENDER_FEMALE = "F"
    GENDER_MALE = "M"
    GENDER_OPTIONS = ((GENDER_FEMALE, "Female"), (GENDER_MALE, "Male"))

    age = models.IntegerField(default=None)
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS, default=None)
    address = models.CharField(max_length=40, blank=True, default="/")
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

    def __str__(self):
        return self.username + " (" + self.symptoms + ")"

    @property
    def get_name(self):
        return self.first_name + " " + self.last_name

    @property
    def get_id(self):
        return self.id

    @property
    def get_status(self):
        return "Approved" if self.status else "Pending"

    def get_profile_pic(self):
        if self.profile_pic:
            return self.profile_pic.url
        else:
            return "/static/assets/profile/img/default/default_profile_picture.png"


class OfficeManager(User):
    address = models.CharField(max_length=254, blank=True, default="/")
    mobile = PhoneNumberField(blank=True)
    profile_pic = models.ImageField(
        upload_to="profile_pic/OfficeManagerProfilePic/", null=True, blank=True
    )

    class Meta:
        verbose_name = "OfficeManager"
        verbose_name_plural = "OfficeManagers"

    def __str__(self):
        return str(self.username)

    def save(self, *args, **kwargs):
        self.is_manager = True
        super().save(*args, **kwargs)

    @property
    def get_id(self):
        return self.id

    def get_profile_pic(self):
        if self.profile_pic:
            return self.profile_pic.url
        else:
            return "/static/assets/profile/img/default/default_profile_picture.png"
