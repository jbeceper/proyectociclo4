from django.contrib.auth.models import User
from django.db.models import fields
from rest_framework import serializers
from .models import Soporte, PQR, Bank
from django.contrib.auth.models import User

class USerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ['username','email']

class SoporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soporte
        fields = '__all__' #Serializar todos los campos

class PQRSerializer(serializers.ModelSerializer):
    soporte = SoporteSerializer()
    class Meta:
        model = PQR
        fields = ['id', 'soporte','tipo','info']

class BankSerializar(serializers.ModelSerializer):
    User=USerSerializer(many=True)
    class Meta:
        model = Bank
        fields = ['id','name','address']