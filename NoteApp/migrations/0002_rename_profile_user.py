# Generated by Django 4.1.2 on 2023-03-04 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("NoteApp", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(old_name="Profile", new_name="user",),
    ]