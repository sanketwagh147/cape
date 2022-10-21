import os
import sys
import django
import pandas as pd
from forecast.models import Forecast

# django.setup()
# sys.path.append('django_apps/mysite/forecast')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')


def run():
    print('reading csv...')
    df = pd.read_csv("https://raw.githubusercontent.com/nathanramoscfa/cape/main/data/cape_return_forecast.csv")
    df.CAPE = df.CAPE.map('{:,.2f}'.format)
    df.FWD_RETURN_5Y_FORECAST = df.FWD_RETURN_5Y_FORECAST.map('{:,.2%}'.format)
    array = df.to_dict(orient='records')
    for entry in array:
        forecast = Forecast(
            etf_ticker=entry['ETF_TICKER'],
            etf_name=entry['ETF_NAME'],
            index_name=entry['INDEX_NAME'],
            cape=entry['CAPE'],
            fwd_return_forecast=entry['FWD_RETURN_5Y_FORECAST'],
            index_ticker=entry['INDEX_TICKER']
        )
        forecast.save()
    print('Saved all entries to database.')
    return


if __name__ == "__main__":
    run()
