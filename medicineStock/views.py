from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, get_list_or_404, redirect
from medicineStock.forms import *
from medicineStock.models import Stock
from django.views import generic



class CreateStock(generic.CreateView):
    template_name = 'stock/stock.html'
    form_class = AddStockForm
    model = Stock
    success_url = reverse_lazy('allstock')

    def post(self, request, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        owner = request.user
        if form.is_valid():
            form.instance.added_by = owner
            return self.form_valid(form)
        else:
            return self.form_invalid(form)



class StockView(generic.ListView):
    template_name = "stock/stocklist.html"
    model = Stock
    context_object_name= 'stocks'


def deleteStock(request, pk):
    Stock.objects.get(id=pk).delete()
    return redirect('allstock')

class EditStock(generic.UpdateView):
    template_name = 'stock/edit_stock.html'
    model = Stock
    form_class = EditStockForm
    success_url = reverse_lazy('allstock')
    