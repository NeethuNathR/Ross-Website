# Generated by Django 4.1.2 on 2023-03-05 11:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("credential", "0004_remove_staffregistration_businessid"),
    ]

    operations = [
        migrations.AddField(
            model_name="staffregistration",
            name="userid",
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
