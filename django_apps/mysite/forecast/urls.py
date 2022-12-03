from django.urls import path
from . import views

app_name = 'forecast'
urlpatterns = [
    path('', views.index, name='index'),
    path('equity_etf_table/', views.equity_etf_table, name='equity_etf_table'),
    path('common_stock_table/', views.common_stock_table, name='common_stock_table'),
    path('bond_etf_table/', views.bond_etf_table, name='bond_etf_table'),
    path('cape_charts/<int:pk>', views.cape_charts, name='cape_charts'),
]
