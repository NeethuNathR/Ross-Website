from django.db import models


class Profile(models.Model):

  businessid=models.CharField(max_length=100)
  businessname=models.CharField(max_length=200)
  contact=models.CharField(max_length=15)
  address=models.CharField(max_length=200)
  pincode=models.IntegerField()
  district=models.CharField(max_length=200)
  state=models.CharField(max_length=200)

class Meta:
    db_table='noteapp_profile'