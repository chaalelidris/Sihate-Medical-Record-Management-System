# Generated by Django 4.1.5 on 2023-04-15 14:09

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_remove_officemanager_address_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="officemanager",
            name="address",
            field=models.CharField(default="/", max_length=254),
        ),
        migrations.AddField(
            model_name="officemanager",
            name="mobile",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True, max_length=128, region=None
            ),
        ),
    ]
