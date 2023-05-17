from django.db import models

# Create your models here.
class Students(models.Model):
    first_name = models.CharField(max_length=15,null=True,blank=True)
    last_name = models.CharField(max_length=15,null=True,blank=True)
    date_or_birth = models.IntegerField(max_length=15,null=True,blank=True)
    mobile_number = models.IntegerField(max_length=10,null=True,blank=True)
    GENDER_TYPES =(
    (1, 'male'),
    (2, 'female'),
    (3, 'other'),
    )
    gender = models.IntegerField(
    choices = GENDER_TYPES,
    default = 1)
class Orders(models.Model):
    oders_name = models.CharField(max_length=15,null=True,blank=True)
    oders_quantity = models.IntegerField(max_length=15,null=True,blank=True)
    oders_discount = models.IntegerField(max_length=15,null=True,blank=True)
    oders_address = models.TextField(max_length=15,null=True,blank=True)
    oders_place_at = models.TextField(max_length=15,null=True,blank=True)
    oders_time = models.TimeField(max_length=15,null=True,blank=True)