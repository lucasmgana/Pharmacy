from django.contrib import admin
from sales.models import Payment, Sale, ModeOfPayment



admin.site.register([Sale, ModeOfPayment, Payment])