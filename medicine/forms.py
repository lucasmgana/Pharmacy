from django import forms
from django.forms import fields
from medicine.models import Medicine

class AddMedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ("medicine_name", "category", "generic_name", "form", "discount", "side_effect", "image")



class UpdateMedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields =  ("medicine_name", "category", "generic_name", "form", "discount", "side_effect", "image")