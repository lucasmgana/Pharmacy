from django.db import models
from django.utils.translation import gettext_lazy as _
from configurations import utils


class Medicine(models.Model):
    id = models.AutoField(primary_key= True)
    medicine_name = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    generic_name = models.CharField(max_length=255)
    form = models.ForeignKey('MedicineForm', on_delete=models.CASCADE, null=True, blank=True)
    discount = models.IntegerField(default=0)
    side_effect = models.CharField(max_length=255,null=True, blank=True)
    slug = models.SlugField(_("identifier"), null=True, blank=True, unique=True)
    image = models.ImageField(null = True, blank = True)
    added_date = models.DateTimeField(auto_now_add=True)
        
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
    slug = models.SlugField(_("identifier"), null=True, blank=True, unique=True)


    def save(self):
        self.slug = utils.slugify(self.title)
        return super().save()

    def __str__(self) -> str:
        return self.title


    class Meta:
        verbose_name_plural = 'Categories'
