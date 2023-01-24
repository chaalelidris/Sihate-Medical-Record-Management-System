from django.db import models

# Create your models here.


class Ordonnance(models.Model):
    id_ordonnance = models.AutoField(primary_key=True)
    # date = models.DateTimeField(auto_now_add=True, blank=True)
    name_patient = models.ForeignKey(
        "FichePatient",
        related_name="ORD_patient",
        on_delete=models.CASCADE,
        default=None,
    )
    date = models.DateTimeField()
    medicament = models.CharField(max_length=254)
    observation = models.TextField(max_length=254)

    def __str__(self):
        return str(self.date)

    def nom(self):
        return self.name_patient.nom

    def prenom(self):
        return self.name_patient.prenom

    def age(self):
        return self.name_patient.age
