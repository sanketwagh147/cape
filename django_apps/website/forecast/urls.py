from django.urls import path
from . import views

app_name = 'forecast'
urlpatterns = [
    path('', views.index, name='index'),
    path('equity_etf_table/', views.equity_etf_table, name='equity_etf_table'),
    path('common_stock_table/', views.common_stock_table, name='common_stock_table'),
    path('bond_etf_table/', views.bond_etf_table, name='bond_etf_table'),
    path('outliers_table/', views.outliers_table, name='outliers_table'),
    path('cape_charts/<int:pk>', views.cape_charts, name='cape_charts'),
    path('subscription/', views.subscription, name='subscription'),
    path('subscribe/free/', views.subscribe_free, name='subscribe_free'),
    path('subscribe/pro_monthly/', views.subscribe_pro_monthly, name='subscribe_pro_monthly'),
    path('subscribe/pro_semiannually/', views.subscribe_pro_semiannually, name='subscribe_pro_semiannually'),
    path('subscribe/pro_annually/', views.subscribe_pro_annually, name='subscribe_pro_annually'),
]
