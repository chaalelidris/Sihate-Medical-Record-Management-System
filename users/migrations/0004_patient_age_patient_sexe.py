# Generated by Django 4.1.5 on 2023-03-14 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "users",
            "0003_rename_consultationdate_consultation_consultation_date_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="age",
            field=models.IntegerField(default="0"),
        ),
        migrations.AddField(
            model_name="patient",
            name="sexe",
            field=models.CharField(
                choices=[("F", "Female"), ("M", "Male"), ("U", "Unsure")],
                default=None,
                max_length=1,
            ),
        ),
    ]
