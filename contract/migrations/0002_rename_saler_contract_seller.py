# Generated by Django 4.0.3 on 2022-03-30 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contract", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contract",
            old_name="saler",
            new_name="seller",
        ),
    ]
