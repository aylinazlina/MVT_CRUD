from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Plants(models.Model):
  id=models.IntegerField(blank=True,primary_key=True)
  name=models.CharField(max_length=200)
  pic=models.ImageField(upload_to='images/',blank=True,null=True,default='images/Default_pic.jpg')
  price=models.FloatField()


  def __str__(self):
      return self.name


