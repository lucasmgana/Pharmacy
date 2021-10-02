from typing import Tuple
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _




class Profile(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    gender = CharField(max_length=255, null=True, blank=True)
    fullname = CharField(max_length=255, null=True, blank=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    nida = models.IntegerField(null=True, blank=True)
    kura = models.IntegerField(null=True, blank=True)
    licence = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(_("Email"), max_length=254)
    location = models.CharField(max_length=255, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True)
    is_boss = models.BooleanField(_("Boss"), default=False)
    

    # medicine perms
    can_add_medicine= models.BooleanField(_("Can Add Medicine?"), default=False)
    can_edit_medicine= models.BooleanField(_("Can Edit Medicine?"), default=False)
    can_delete_medicine= models.BooleanField(_("Can Delete Medicine?"), default=False)

    # stock perms
    can_add_stock= models.BooleanField(_("Can Add Stock?"), default=False)
    can_edit_stock= models.BooleanField(_("Can Edit Stock?"), default=False)
    can_delete_stock= models.BooleanField(_("Can Delete Stock?"), default=False)

    # sales perms
    can_add_sales= models.BooleanField(_("Can Make Sales?"), default=False)
    can_edit_sales= models.BooleanField(_("Can Change Sales?"), default=False)
    can_delete_sales= models.BooleanField(_("Can Remove Sales?"), default=False)

    # staff perms
    can_add_salesman= models.BooleanField(_("Can Add Salesman?"), default=False)
    can_delete_salesman= models.BooleanField(_("Can Delete Salesman?"), default=False)
    can_edit_salesman= models.BooleanField(_("Can Modify Salesman?"), default=False)
    can_lock_salesman= models.BooleanField(_("Can Block Salesman?"), default=False)
    can_generate_report= models.BooleanField(_("Can Print Report?"), default=False)


    def __str__(self) -> str:
        return str(self.owner)
        


class Expense(models.Model):
    id = models.CharField(max_length=255, primary_key= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(max_length=255)
    service_name = models.CharField(max_length=255)
    expense_name = models.CharField(max_length=255)
    price = models.IntegerField()
        
    def __str__(self) -> str:
        return self.expense_name


