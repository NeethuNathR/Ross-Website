# Generated by Django 4.1.2 on 2023-03-04 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("NoteApp", "0003_alter_user_contact"),
    ]

    operations = [
        migrations.RenameModel(old_name="user", new_name="Profile",),
    ]