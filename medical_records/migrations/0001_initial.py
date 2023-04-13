# Generated by Django 4.1.5 on 2023-04-13 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="MedicalRecord",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "group_sanguin",
                    models.CharField(
                        choices=[
                            ("O+", "O+"),
                            ("O-", "O-"),
                            ("A+", "A+"),
                            ("A-", "A-"),
                            ("B+", "B+"),
                            ("B-", "B-"),
                            ("AB+", "AB+"),
                            ("AB-", "AB-"),
                        ],
                        default=None,
                        max_length=3,
                    ),
                ),
                ("NSS", models.CharField(max_length=254)),
                ("profession", models.CharField(max_length=254)),
                ("establishment_name", models.CharField(max_length=254)),
                ("birthday", models.DateField()),
                ("birthday_location", models.CharField(max_length=254)),
                (
                    "situation",
                    models.CharField(
                        choices=[
                            ("celebataire", "Celebataire"),
                            ("Maried", "Maried"),
                            ("Divorced", "Divorced"),
                            ("Widower", "Widower"),
                        ],
                        default=None,
                        max_length=11,
                    ),
                ),
                (
                    "smocking",
                    models.CharField(
                        choices=[("Oui", "Yes"), ("Non", "NO")],
                        default=None,
                        max_length=3,
                    ),
                ),
                ("general_maladies", models.TextField(max_length=254)),
                ("allergic_reactions_to_drugs", models.TextField(max_length=254)),
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="doctor_medical_file",
                        to="users.doctor",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="patient_medical_file",
                        to="users.patient",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Prescription",
            fields=[
                (
                    "id_prescription",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("medication", models.CharField(max_length=254)),
                ("duration", models.IntegerField()),
                ("observation", models.TextField(max_length=254)),
                ("date_prescribed", models.DateTimeField()),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="patient_medical_file",
                        to="medical_records.medicalrecord",
                    ),
                ),
            ],
        ),
    ]
