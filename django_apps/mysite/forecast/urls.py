from django.urls import path
from . import views

app_name = 'forecast'
urlpatterns = [
    path('', views.index, name='index'),
    path('forecast_table/', views.forecast_table, name='forecast_table'),
    path('forecast_charts/<int:pk>', views.forecast_charts, name='forecast_charts'),
]
