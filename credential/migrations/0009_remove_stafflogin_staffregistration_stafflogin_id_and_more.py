# Generated by Django 4.1.2 on 2023-03-07 05:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        (
            "credential",
            "0008_remove_stafflogin_id_remove_staffregistration_id_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(model_name="stafflogin", name="staffregistration",),
        migrations.AddField(
            model_name="stafflogin",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                default=django.utils.timezone.now,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="stafflogin",
            name="password",
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="stafflogin",
            name="username",
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="stafflogin",
            name="userid",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="credential.staffregistration",
            ),
        ),
    ]
