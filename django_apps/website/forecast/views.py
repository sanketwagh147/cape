from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Forecast, UserSubscription


@login_required
def subscription(request):
    user_subscription = UserSubscription.objects.get(user=request.user)
    context = {'user_subscription': user_subscription}
    return render(request, 'subscription.html', context)


@login_required
def subscribe_free(request):
    # Logic to handle free subscription
    return redirect('some_url')


@login_required
def subscribe_pro_monthly(request):
    # Logic to handle monthly subscription
    return redirect('some_url')


@login_required
def subscribe_pro_semiannually(request):
    # Logic to handle semiannually subscription
    return redirect('some_url')


@login_required
def subscribe_pro_annually(request):
    # Logic to handle annually subscription
    return redirect('some_url')


@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def equity_etf_table(request):
    if not has_access(request.user, 'Equity ETF'):
        return redirect('subscription')
    data = Forecast.objects.filter(security_type='Equity ETF').order_by('-fwd_return_forecast')
    context = {'data': data}
    return render(request, 'equity_etf_table.html', context)


@login_required
def common_stock_table(request):
    if not has_access(request.user, 'Common Stock'):
        return redirect('subscription')
    data = Forecast.objects.filter(security_type='Common Stock').order_by('-fwd_return_forecast')
    context = {'data': data}
    return render(request, 'common_stock_table.html', context)


@login_required
def bond_etf_table(request):
    if not has_access(request.user, 'Bond ETF'):
        return redirect('subscription')
    data = Forecast.objects.filter(security_type='Bond ETF').order_by('-fwd_return_forecast')
    context = {'data': data}
    return render(request, 'bond_etf_table.html', context)


@login_required
def outliers_table(request):
    if not has_access(request.user):
        return redirect('subscription')
    data = Forecast.objects.filter(outlier_bool=True).order_by('-fwd_return_forecast')
    context = {'data': data}
    return render(request, 'outliers_table.html', context)


@login_required
def cape_charts(request, pk):
    if not has_access(request.user):
        return redirect('subscription')
    charts = Forecast.objects.get(pk=pk)
    context = {'charts': charts}
    return render(request, 'cape_charts.html', context)


def has_access(user, security_type=None):
    try:
        user_subscription = UserSubscription.objects.get(user=user)
        if user_subscription.plan.name == 'free':
            if security_type and security_type not in ['SPY', 'DIA', 'QQQ']:
                return False
        return True
    except UserSubscription.DoesNotExist:
        return False
