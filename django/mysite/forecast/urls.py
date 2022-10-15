from django.urls import path
from . import views

app_name = 'forecast'
urlpatterns = [
    path('', views.index, name='index'),
    path('', views.Table, name='forecast_table'),
]
