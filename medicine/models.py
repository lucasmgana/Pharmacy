from django.db import models




class Medicine(models.Model):
    id = models.CharField(max_length=255, primary_key= True)
    medicine_name = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    generic_name = models.CharField(max_length=255)
    form = models.ForeignKey('MedicineForm', on_delete=models.CASCADE, null=True, blank=True)
    discount = models.IntegerField(default=0)
    side_effect = models.CharField(max_length=255,null=True, blank=True)
    image = models.ImageField(null = True, blank = True)
        
    def __str__(self) -> str:
        return self.medicine_name

class MedicineForm(models.Model):
    id = models.CharField(max_length=255, primary_key= True)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    id = models.CharField(max_length=255, primary_key= True)
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

