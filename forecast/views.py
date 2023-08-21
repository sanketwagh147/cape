from django.shortcuts import render, redirect
from .models import Forecast


def index(request):
    return render(request, 'index.html')


def equity_etf_table(request):
    data = Forecast.objects.filter(security_type='Equity ETF').order_by('-fwd_return_forecast')
    context = {'data': data}
    return render(request, 'equity_etf_table.html', context)


def common_stock_table(request):
    data = Forecast.objects.filter(security_type='Common Stock').order_by('-fwd_return_forecast')
    context = {'data': data}
    return render(request, 'common_stock_table.html', context)


def bond_etf_table(request):
    data = Forecast.objects.filter(security_type='Bond ETF').order_by('-fwd_return_forecast')
    context = {'data': data}
    return render(request, 'bond_etf_table.html', context)


def outliers_table(request):
    data = Forecast.objects.filter(outlier_bool=True).order_by('-fwd_return_forecast')
    context = {'data': data}
    return render(request, 'outliers_table.html', context)


def cape_charts(request, pk):
    charts = Forecast.objects.get(pk=pk)
    context = {'charts': charts}
    return render(request, 'cape_charts.html', context)
