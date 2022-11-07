from django.shortcuts import get_object_or_404, render
from .models import Forecast


def index(request):
    return render(request, 'index.html')


def forecast_table(request):
    data = Forecast.objects.all().order_by('-fwd_return_forecast')
    context = {'data': data}
    return render(request, 'forecast_table.html', context)


def forecast_charts(request, pk):
    charts = Forecast.objects.get(pk=pk)
    context = {'charts': charts}
    return render(request, 'forecast_charts.html', context)
