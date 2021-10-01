from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):
    id = models.CharField(max_length=255, primary_key= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(max_length=255)
    service_name = models.CharField(max_length=255)
    expense_name = models.CharField(max_length=255)
    price = models.IntegerField()
        
    def __str__(self) -> str:
        return self.expense_name


class PharmPermission(models.Model):
    id = models.CharField(max_length=255, primary_key= True)
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Profile(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    dob = models.DateField()
    mobile = models.IntegerField()
    location = models.CharField(max_length=255)
    profile_image = models.ImageField()
    
    def __str__(self) -> str:
        return str(self.owner)


class ProfilePerm(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True, blank=True)
    permission = models.ForeignKey('PharmPermission', on_delete=models.CASCADE, null=True, blank=True)
