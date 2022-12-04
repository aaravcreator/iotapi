from django.contrib import admin
from .models import Sensor,Led
# Register your models here.
admin.site.register(Sensor)
admin.site.register(Led)