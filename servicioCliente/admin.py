from django.contrib import admin
from .models import PQR, Soporte, Bank

# Register your models here.
admin.site.register(Soporte)
admin.site.register(PQR)
admin.site.register(Bank)