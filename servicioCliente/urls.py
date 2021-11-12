from django.urls import path, include
from .views import CountUser, SoporteListCreate, SoporteUpdateDelete, PQRListCreate, PQRUpdateDelete, BankListCreate
urlpatterns = [
    path('soporte/',SoporteListCreate.as_view()),
    path('soporte/<pk>/',SoporteUpdateDelete.as_view), #Espera una variable <>
    path('pqr/',PQRListCreate.as_view()),
    path('pqr/<pk>/', PQRUpdateDelete.as_view()),
    path('bank/',BankListCreate.as_view()),
    path('number-users/',CountUser.as_view())
]