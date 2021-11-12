from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import views, generics, authentication, permissions, status
from rest_framework.response import Response
from .models import Bank, Soporte,PQR
from servicioCliente.models import Soporte
from .serializer import BankSerializar, SoporteSerializer, PQRSerializer
from rest_framework import generics, authentication, permissions
from django.contrib.auth.models import User

# Create your views here.

class SoporteListCreate(generics.ListCreateAPIView):
    queryset = Soporte.objects.all()
    serializer_class = SoporteSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class SoporteUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Soporte.objects.all()
    serializer_class = SoporteSerializer

class PQRListCreate(generics.ListCreateAPIView):
    queryset = PQR.objects.all()
    serializer_class = PQRSerializer

class PQRUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = PQR.objects.all()
    serializer_class = PQRSerializer

class BankListCreate(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializar

class CountUser(views.APIView):
    def get(self, request):
        request.data
        queryset = User.objects.all()
        con_users = len(queryset)
        data={"Number of users": con_users}
        return Response(data=data, status=status.HTTP_200_OK)


