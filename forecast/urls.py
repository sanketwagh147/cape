from django.urls import path
from . import views
from . import payment_views

app_name = 'forecast'
urlpatterns = [
    path('', views.index, name='index'),

    path('subscribe/', payment_views.subscribe, name='subscribe'),
    path('stripe/webhook/', payment_views.stripe_webhook, name='stripe-webhook'),
    path('stripe/config/', payment_views.stripe_configuration, name="stripe-config"),
    path('create-checkout-session/', payment_views.create_checkout_session, name="stripe-session-creation"),

    path('equity_etf_table/', views.equity_etf_table, name='equity_etf_table'),
    path('common_stock_table/', views.common_stock_table, name='common_stock_table'),
    path('bond_etf_table/', views.bond_etf_table, name='bond_etf_table'),
    path('outliers_table/', views.outliers_table, name='outliers_table'),
    path('cape_charts/<int:pk>', views.cape_charts, name='cape_charts'),
]
