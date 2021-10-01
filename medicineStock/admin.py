from django.contrib import admin
from medicineStock.models import Purchase, Stock


admin.site.register([Stock, Purchase])