from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Sensor(models.Model):
    temp = models.CharField(max_length=5,)
    humidity = models.CharField(max_length=5)
    remarks = models.CharField(max_length=100,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="sensors")


class Led(models.Model):
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="leds")