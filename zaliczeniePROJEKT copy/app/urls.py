# urls.py
from django.urls import path
from .views import fuel_calculation

urlpatterns = [
    path('', fuel_calculation, name='fuel_calculation'),
]
