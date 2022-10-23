from django.shortcuts import render
from .models import Forecast


def index(request):
    return render(request, 'index.html')


def forecast_table(request):
    data = Forecast.objects.all().order_by('-fwd_return_forecast').values()
    context = {'d': data}
    if data:
        print('working')
    return render(request, 'forecast_table.html', context)
