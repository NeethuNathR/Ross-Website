# Generated by Django 4.1.2 on 2023-03-05 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("credential", "0005_staffregistration_userid"),
    ]

    operations = [
        migrations.CreateModel(
            name="staffLogin",
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
                    "userid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="credential.staffregistration",
                    ),
                ),
            ],
        ),
    ]
