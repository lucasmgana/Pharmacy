from django.db.models.query import QuerySet
from medicine.forms import AddMedicineForm

from django.shortcuts import get_object_or_404, get_list_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from .models import *


class ManageMedicine(generic.TemplateView):
    template_name= "medicine/manage_medicine.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["medicines"] = Medicine.objects.all()
        return context
    


class AddMedicine(generic.CreateView):
    model = Medicine
    form_class = AddMedicineForm
    template_name = 'medicine/add_medicine.html'
    success_url = reverse_lazy('manage_medicine')


class EditMedicine(generic.UpdateView):
    model = Medicine
    form_class = AddMedicineForm
    template_name = 'medicine/edit_medicine.html'
    success_url = reverse_lazy('manage_medicine')


def deleteMedicine(request, pk):
    Medicine.objects.get(id=pk).delete()
    return redirect('manage_medicine')
