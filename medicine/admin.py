from django.contrib import admin
from medicine.models import Medicine, MedicineForm, Category


admin.site.register([
    Medicine, MedicineForm, Category
    ])
