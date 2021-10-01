from django.db import models


class Stock(models.Model):
    id = models.CharField(max_length=255, primary_key= True)
    medicine_id = models.ForeignKey('medicine.Medicine', on_delete=models.CASCADE, null=True, blank=True)
    expire_date = models.DateField()
    quantity = models.IntegerField()
    buying_price = models.IntegerField()
    Selling_price = models.IntegerField()
    profit = models.IntegerField()
    added_by = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return str(self.medicine_id)

        
class Purchase(models.Model):
    id = models.CharField(max_length=255, primary_key= True)
    name = models.CharField(max_length=255)
    due_date = models.DateField()
    buying_price = models.IntegerField()
    quantity = models.IntegerField()
        
    def __str__(self) -> str:
        return self.name
