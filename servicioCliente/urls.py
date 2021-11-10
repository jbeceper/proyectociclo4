from django.urls import path, include
from .views import SoporteListCreate, SoporteUpdateDelete, PQRListCreate, PQRUpdateDelete

urlpatterns = [
    path('soporte/',SoporteListCreate.as_view()),
    path('soporte/<pk>/',SoporteUpdateDelete.as_view), #Espera una variable <>
    path('pqr/',PQRListCreate.as_view()),
    path('pqr/<pk>/', PQRUpdateDelete.as_view())
]