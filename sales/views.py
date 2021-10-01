from django.views import generic


class SaleView(generic.TemplateView):
    template_name= "sales/sales.html"