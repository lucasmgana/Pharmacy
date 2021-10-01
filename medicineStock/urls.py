from django.urls import path
from medicineStock import views as stockViews

urlpatterns = [
    path('', stockViews.StockView.as_view(), name='allStock')
]
