import os
import sys
import django
import pandas as pd

django.setup()
sys.path.append('django_apps/mysite/forecast')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

from forecast.models import Forecast


def run():
    print('reading csv...')
    df = pd.read_csv("https://raw.githubusercontent.com/nathanramoscfa/cape/main/data/cape_return_forecast.csv")
    df.CAPE = df.CAPE.map('{:,.2f}'.format)
    df.FWD_RETURN_5Y_FORECAST = df.FWD_RETURN_5Y_FORECAST.map('{:,.2%}'.format)
    df.LOWER_CONFIDENCE = df.LOWER_CONFIDENCE.map('{:,.2%}'.format)
    df.UPPER_CONFIDENCE = df.UPPER_CONFIDENCE.map('{:,.2%}'.format)
    for ticker in Forecast.objects.values_list('etf_ticker'):
        forecast = Forecast.objects.get(etf_ticker=ticker)
        forecast.etf_ticker = df[df['ETF_TICKER'] == ticker].ETF_TICKER
        forecast.etf_name = df[df['ETF_TICKER'] == ticker].ETF_NAME
        forecast.index_name = df[df['ETF_TICKER'] == ticker].INDEX_NAME
        forecast.cape = df[df['ETF_TICKER'] == ticker].CAPE
        forecast.fwd_return_forecast = df[df['ETF_TICKER'] == ticker].FWD_RETURN_5Y_FORECAST
        forecast.lower_confidence = df[df['ETF_TICKER'] == ticker].LOWER_CONFIDENCE
        forecast.upper_confidence = df[df['ETF_TICKER'] == ticker].UPPER_CONFIDENCE
        forecast.index_ticker = df[df['ETF_TICKER'] == ticker].INDEX_TICKER
        forecast.expected_fwd_return_chart = 'expected_fwd_return_5y_{}.jpg'.format(
            df[df['ETF_TICKER'] == ticker].INDEX_TICKER)
        forecast.long_term_pe_ratio_chart = 'long_term_pe_ratio_{}.jpg'.format(
            df[df['ETF_TICKER'] == ticker].INDEX_TICKER)
        forecast.sample_observed_forecast_chart = 'sample_observed_forecast_{}.jpg'.format(
            df[df['ETF_TICKER'] == ticker].INDEX_TICKER)
        forecast.sample_regression_chart = 'sample_regression_{}.jpg'.format(
            df[df['ETF_TICKER'] == ticker].INDEX_TICKER)
        forecast.save()
    print('Saved all entries to database.')
    return


if __name__ == "__main__":
    run()
