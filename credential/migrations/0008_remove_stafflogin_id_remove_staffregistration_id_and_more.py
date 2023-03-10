# Generated by Django 4.1.2 on 2023-03-06 05:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("credential", "0007_alter_stafflogin_userid"),
    ]

    operations = [
        migrations.RemoveField(model_name="stafflogin", name="id",),
        migrations.RemoveField(model_name="staffregistration", name="id",),
        migrations.AddField(
            model_name="stafflogin",
            name="staffregistration",
            field=models.ForeignKey(
                default=django.utils.timezone.now,
                on_delete=django.db.models.deletion.CASCADE,
                to="credential.staffregistration",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="stafflogin",
            name="userid",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="staffregistration",
            name="userid",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
