from django.urls import path
from pharmaProfile import views as userViews


urlpatterns = [
    path('', userViews.SalesManRegisterView.as_view(), name='profile'),
    path('permit/<int:pk>/', userViews.PermitSalesman.as_view(), name='permit'),
    path('users/', userViews.ManageUser.as_view(), name='users'),
]
