from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Models


class Medical_office(models.Model):
    id_office = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    email = models.EmailField()
    tel = PhoneNumberField(blank=True)
    fax = PhoneNumberField(blank=True)

    def __str__(self):
        return str(self.Name)
