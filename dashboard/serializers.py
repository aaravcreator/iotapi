from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models  import User
from .models import Sensor,Led

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SensorSerializer(ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('temp','humidity')

class LedSerializer(ModelSerializer):
    class Meta:
        model = Led
        fields = ('status',)
