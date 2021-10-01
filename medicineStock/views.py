from django.views import generic




class StockView(generic.TemplateView):
    template_name = 'stock/stock.html'