from django import forms
from django.forms import fields
from medicineStock.models import Stock


class AddStockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields =(
            'medicine_id', 'expire_date', 'quantity', 
            'buying_price', 'selling_price'
            )


class EditStockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields =(
            'medicine_id', 'expire_date', 'quantity', 
            'buying_price', 'selling_price',
            )
        