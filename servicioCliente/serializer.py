from django.db.models import fields
from rest_framework import serializers
from .models import Soporte, PQR

class SoporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soporte
        fields = '__all__' #Serializar todos los campos

class PQRSerializer(serializers.ModelSerializer):
    soporte = SoporteSerializer()
    class Meta:
        model = PQR
        fields = ['id', 'soporte','tipo','info']