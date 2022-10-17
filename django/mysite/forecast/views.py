from django.shortcuts import render
import pandas as pd
import json


def index(request):
    return render(request, 'index.html')

def Table(request):
    df = pd.read_csv("https://raw.githubusercontent.com/nathanramoscfa/cape/main/data/cape_return_forecast.csv")
    df.CAPE = df.CAPE.map('{:,.2f}'.format)
    df.FWD_RETURN_5Y_FORECAST = df.FWD_RETURN_5Y_FORECAST.map('{:,.2%}'.format)
    json_records = df.reset_index().to_json(orient='records')
    data = json.loads(json_records)
    context = {'d': data}

    return render(request, 'forecast_table.html', context)
