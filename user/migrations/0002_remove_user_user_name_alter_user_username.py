# Generated by Django 4.0.3 on 2022-03-25 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="user_name",
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
