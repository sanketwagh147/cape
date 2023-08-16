from datetime import timedelta
from django.utils import timezone
from django.shortcuts import render, redirect
from .models import Forecast, Subscription
from django.contrib.auth.decorators import login_required


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


@login_required
def subscribe(request, plan_type):
    # Here, you can integrate with a payment gateway like Stripe or PayPal
    # You may want to check the plan_type variable to match the appropriate plan
    # and set the price accordingly.

    # Create a Subscription object for the user
    subscription = Subscription(name=plan_type, user=request.user)
    if plan_type == Subscription.MONTHLY:
        subscription.price = 30
    elif plan_type == Subscription.SEMI_ANNUAL:
        subscription.price = 150
    elif plan_type == Subscription.ANNUAL:
        subscription.price = 300

    # Set trial period if needed
    if plan_type != Subscription.FREE:
        subscription.trial_ends_at = timezone.now() + timedelta(days=30)

    subscription.save()

    # Redirect to success page
    return redirect('success_page')


@login_required
def view_content(request, ticker):
    user_subscription = Subscription.objects.get(user=request.user)
    if user_subscription.name == Subscription.FREE and ticker != 'AAPL':
        return redirect('subscribe_page')  # Redirect to subscription page
    else:
        # Retrieve the content related to the specific ticker
        content = Forecast.objects.get(ticker=ticker)

        # Render a template, passing the content to it
        return render(request, 'forecast/ticker_detail.html', {'content': content})
