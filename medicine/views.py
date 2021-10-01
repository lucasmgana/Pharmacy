from django.db.models.query import QuerySet
from medicine.forms import AddMedicineForm

from django.shortcuts import get_object_or_404, get_list_or_404
from django.views import generic
from django.urls import reverse_lazy
from .models import *


class ManageMedicine(generic.ListView):
    template_name= "medicine/manage_medicine.html"
    # queryset= Medicine
    model= Medicine
    context_object_name='medicines'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["medicine"] = get_list_or_404(Medicine)
    #     return context
    


class AddMedicine(generic.CreateView):
    model = Medicine
    form_class = AddMedicineForm
    template_name = 'medicine/add_medicine.html'
    success_url = reverse_lazy('manage_medicine')


class EditMedicine(generic.UpdateView):
    model = Medicine
    form_class = AddMedicineForm
    template_name = 'medicine/edit_medicine.html'
    success_url = reverse_lazy('homepage')


class DeleteMedicine(generic.DeleteView):
    model = Medicine
    template_name = 'medicine/manage_medicine.html'
    success_url = reverse_lazy('homepage')

