from django import urls
from django.urls import  path
from medicine import views as medicineViews


urlpatterns = [
    path('', medicineViews.ManageMedicine.as_view(), name='manage_medicine'),
    path('add_medicine/', medicineViews.AddMedicine.as_view(), name = 'add_medicine'),
    path('edit_medicine/<int:pk>/', medicineViews.EditMedicine.as_view(), name = 'edit_medicine'),
    path('delete_medicine/<int:pk>/', medicineViews.deleteMedicine, name = 'delete_medicine'),
]
