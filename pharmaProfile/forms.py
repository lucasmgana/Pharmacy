from django import forms
from django.forms.widgets import CheckboxInput, EmailInput, NumberInput, TextInput


class RegisterSalesmanForm(forms.Form):

    """
    RegisterSalesman definition.
    TODO: 
        Define form fields here
        add user without any permission
    """
    first_name = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))
    middle_name = forms.CharField(required=False, widget=TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(required=True, widget=TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=EmailInput(attrs={'class': 'form-control'}))
    nida = forms.IntegerField(widget=NumberInput(attrs={'class': 'form-control'}))
    licence = forms.IntegerField(widget=NumberInput(attrs={'class': 'form-control'}))
    kura = forms.IntegerField(widget=NumberInput(attrs={'class': 'form-control'}))
    mobile_number = forms.IntegerField(required=True, widget=NumberInput(attrs={'class': 'form-control'}))


class PermitSalesmanForm(forms.Form):
    
    """
    RegisterSalesman definition.
    TODO: 
        granting user permissions
    """
    is_boss = forms.BooleanField(required=False, widget=CheckboxInput(attrs={'class':'form-control'}), initial=False)
    can_add_medicine = forms.BooleanField(required=False, widget=CheckboxInput(attrs={'class':'form-control'}), initial=False)
    can_edit_medicine = forms.BooleanField(required=False, widget=CheckboxInput(attrs={'class':'form-control'}), initial=False)
    can_delete_medicine = forms.BooleanField(required=False, widget=CheckboxInput(attrs={'class':'form-control'}), initial=False)
    can_add_stock = forms.BooleanField(required=False, widget=CheckboxInput(attrs={'class':'form-control'}), initial=False)
    can_edit_stock = forms.BooleanField(required=False, widget=CheckboxInput(attrs={'class':'form-control'}), initial=False)
    can_delete_stock = forms.BooleanField(required=False, widget=CheckboxInput(attrs={'class':'form-control'}), initial=False)
    can_add_sales = forms.BooleanField(required=False, widget=CheckboxInput(attrs={'class':'form-control'}), initial=True)
    can_edit_sales = forms.BooleanField(required=False, widget=CheckboxInput(attrs={'class':'form-control'}), initial=False)
    can_delete_sales = forms.BooleanField(required=False, widget=CheckboxInput(attrs={'class':'form-control'}), initial=False)
    can_add_salesman = forms.BooleanField(required=False, widget=CheckboxInput(attrs={'class':'form-control'}), initial=False)
    can_delete_salesman = forms.BooleanField(required=False, widget=CheckboxInput(attrs={'class':'form-control'}), initial=False)
    can_edit_salesman = forms.BooleanField(required=False, widget=CheckboxInput(attrs={'class':'form-control'}), initial=False)
    can_lock_salesman = forms.BooleanField(required=False, widget=CheckboxInput(attrs={'class':'form-control'}), initial=False)
    can_generate_report = forms.BooleanField(required=False, widget=CheckboxInput(attrs={'class':'form-control'}), initial=False)