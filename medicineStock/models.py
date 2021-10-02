from django.db import models
from django.forms.models import ModelFormMetaclass
import datetime


class Stock(models.Model):
    id = models.AutoField(primary_key= True)
    medicine_id = models.ForeignKey('medicine.Medicine', on_delete=models.CASCADE, null=True, blank=True)
    expire_date = models.DateField(blank=True, null=True)
    quantity = models.IntegerField(null=True, blank=True)
    buying_price = models.IntegerField(null=True, blank=True)
    selling_price = models.IntegerField(null=True, blank=True)
    added_by = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return str(self.medicine_id)

    @property
    def profit(self):
        profit = ((self.selling_price - self.buying_price)/self.buying_price)*100
        if profit < 0:
            return  "Loss "+str(round(profit, 2)) + "%"
            
        return  str(round(profit, 2)) + "%"
    
    @property
    def expired(self):
        exp = self.expire_date
        today =  datetime.date.today()
        if exp <= today:
            return True
        
        else:
            return False

    @property
    def soonexpired(self):
        diff = self.expire_date - datetime.date.today()
        if ((diff.days) <= 5) and ((diff.days) > 0):
            return True        
        else:
            return False


class Purchase(models.Model):
    id = models.AutoField(primary_key= True)
    stock_name = models.CharField(max_length=255, null=True, blank=True)
    due_date = models.DateField(auto_now_add=True, null=True, blank=True)
    selling_price = models.IntegerField(null=True, blank=True)
    buying_price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    expire_date = models.DateField(blank=True, null=True)
    added_by = models.CharField(max_length=255, null=True, blank=True)
        
    def __str__(self) -> str:
        return self.stock_name
