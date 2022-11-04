from django.urls import path
from . import views
from .views import ChartView

app_name = 'forecast'
urlpatterns = [
    path('', views.index, name='index'),
    path('forecast_table/', views.forecast_table, name='forecast_table'),
    path('forecast_charts/<str:ticker>', ChartView.as_view(), name='charts')
]
