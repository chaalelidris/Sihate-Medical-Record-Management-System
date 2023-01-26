from django.db import models

# prescription/models.


class Prescription(models.Model):
    id_ordonnance = models.AutoField(primary_key=True)
    name_patient = models.ForeignKey(
        "medicalfile.FichePatient",
        related_name="fiche_patient",
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
