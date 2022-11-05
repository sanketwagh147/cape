from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Forecast


def index(request):
    return render(request, 'index.html')


def forecast_table(request):
    data = Forecast.objects.all().order_by('-fwd_return_forecast')
    context = {'d': data}
    return render(request, 'forecast_table.html', context)


class ChartView(TemplateView):
    template_name = 'forecast_charts.html'

    def get(self, request, ticker=None):
        if ticker:
            return render(request, self.template_name, {'ticker': ticker})
        else:
            return render(request, self.template_name)
