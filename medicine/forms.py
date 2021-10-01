from django import forms
from django.forms import fields
from medicine.models import Medicine

class AddMedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'

class UpdateMedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'