from django.shortcuts import render, redirect
from .models import Forecast
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.http import HttpResponse
import typing


def index(request):
    return render(request, 'index.html')


def can_show_more(user: typing.Callable) -> bool:
    if user.is_authenticated:
        if user.is_superuser:
            return True
        else:
            if user.get_subscription_status() == "active":
                return True
            else:
                return False
    else:
        return False


def equity_etf_table(request):
    data = Forecast.objects\
        .filter(security_type='Equity ETF')\
    
    if not can_show_more(request.user):
        data = data\
            .filter(ticker__in=settings.EQUITY_ETF_FOR_FREE_USAGE)
    
    data = data\
        .order_by('-fwd_return_forecast')
    
    context = {'data': data}
    return render(request, 'equity_etf_table.html', context)


def common_stock_table(request):
    data = Forecast.objects\
        .filter(security_type='Common Stock')
    
    if not can_show_more(request.user):
        data = data\
            .filter(ticker__in=settings.COMMON_STOCK_FOR_FREE_USAGE)
    
    data = data\
        .order_by('-fwd_return_forecast')
    
    context = {'data': data}
    return render(request, 'common_stock_table.html', context)


def bond_etf_table(request):
    data = Forecast.objects\
        .filter(security_type='Bond ETF')
    
    if not can_show_more(request.user):
        data = data\
            .filter(ticker__in=settings.BOND_ETF_FOR_FREE_USAGE)
    
    data = data\
        .order_by('-fwd_return_forecast')
    
    context = {'data': data}
    return render(request, 'bond_etf_table.html', context)


def outliers_table(request):
    data = Forecast.objects\
        .filter(outlier_bool=True)\
        .order_by('-fwd_return_forecast')
    
    context = {'data': data}
    return render(request, 'outliers_table.html', context)


def cape_charts(request, pk):
    if can_show_more(request.user):
        charts = Forecast.objects.get(pk=pk)
        context = {'charts': charts}
    else:
        charts = Forecast.objects.filter(
            ticker__in=[
                *settings.EQUITY_ETF_FOR_FREE_USAGE,
                *settings.COMMON_STOCK_FOR_FREE_USAGE,
                *settings.BOND_ETF_FOR_FREE_USAGE
            ],
            pk=pk
        )\
        .first()

        if not charts:
            return redirect("forecast:index")
        else:
            context = {'charts': charts}

    return render(request, 'cape_charts.html', context)
