from django.db import models
from django.contrib.auth.models import User


class Sale(models.Model):
    id = models.CharField(max_length=255, primary_key= True)
    medicine_id = models.ForeignKey('medicine.Medicine', on_delete=models.CASCADE, null=True, blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    due_date = models.DateField()
    quantity = models.IntegerField()
    payment_id = models.ForeignKey('Payment', on_delete=models.CASCADE, null=True, blank=True)
    selling_price = models.IntegerField()
        
    def __str__(self) -> str:
        return str(self.medicine_id)

class ModeOfPayment(models.Model):
    id = models.CharField(max_length=255, primary_key= True)
    mode_of_payment = models.CharField(max_length=255)
        
    def __str__(self) -> str:
        return self.mode_of_payment


class Payment(models.Model):
    id = models.CharField(max_length=255, primary_key= True)
    mode_of_payment = models.ForeignKey('ModeOfPayment', on_delete=models.CASCADE, null=True, blank=True)
    amount = models.IntegerField()
    due_date = models.DateField()
    NHIF_no = models.CharField(max_length=255)
        
    def __str__(self) -> str:
        return str(self.mode_of_payment)

