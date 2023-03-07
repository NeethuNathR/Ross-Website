from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from NoteApp.models import Profile


class StaffRegistration(models.Model):

  userid=models.IntegerField(primary_key=True)
  username=models.CharField(max_length=200)
  designation=models.CharField(max_length=200)
  contact=models.CharField(max_length=15)
  address=models.CharField(max_length=200)
  pincode=models.IntegerField()
  district=models.CharField(max_length=200)
  state=models.CharField(max_length=200)


class Meta:
    db_table='noteapp_StaffRegistration'






class staffLogin(models.Model):
  userid=models.ForeignKey(StaffRegistration,on_delete=models.CASCADE)
  username=models.CharField(max_length=200)
  password=models.CharField(max_length=10)

class Contact(models.Model):
  FullName=models.CharField(max_length=100)
  Email=models.EmailField(max_length=100)
  Subject=models.CharField(max_length=200)
  Message=models.CharField(max_length=250)


