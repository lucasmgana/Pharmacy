from django.urls import path
from pharmaProfile import views as userViews


urlpatterns = [
    path('', userViews.Profile.as_view(), name='profile'),
]
