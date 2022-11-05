import os
import sys
import django
import pandas as pd

django.setup()
sys.path.append('django_apps/mysite/forecast')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

from forecast.models import Charts


def run():
    print('reading csv...')
    df = pd.read_csv("https://raw.githubusercontent.com/nathanramoscfa/cape/main/data/cape_return_forecast.csv")
    array = df.to_dict(orient='records')
    for entry in array:
        charts = Charts(
            index_ticker=entry['INDEX_TICKER'],
            expected_fwd_return="https://github.com/nathanramoscfa/cape/blob/branch1/django_apps/mysite/forecast/static/forecast/images/expected_fwd_return_5y_{}.jpg".format(entry['INDEX_TICKER']),
            long_term_pe_ratio="https://github.com/nathanramoscfa/cape/blob/branch1/django_apps/mysite/forecast/static/forecast/images/long_term_pe_ratio_{}.jpg".format(entry['INDEX_TICKER']),
            sample_observed_forecast="https://github.com/nathanramoscfa/cape/blob/branch1/django_apps/mysite/forecast/static/forecast/images/sample_observed_forecast_{}.jpg".format(entry['INDEX_TICKER']),
            sample_regression="https://github.com/nathanramoscfa/cape/blob/branch1/django_apps/mysite/forecast/static/forecast/images/sample_regression_{}.jpg".format(entry['INDEX_TICKER']),
        )
        charts.save()
    print('Saved all entries to database.')
    return


if __name__ == "__main__":
    run()
