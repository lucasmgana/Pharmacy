from django.urls import path
from sales import views as salesViews


urlpatterns = [
    path('', salesViews.SaleView.as_view(), name='sales'),
]
