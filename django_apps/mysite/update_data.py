import os
import sys
import django
import pandas as pd
from tqdm import tqdm

django.setup()
sys.path.append('django_apps/mysite/forecast')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

from forecast.models import Forecast


def run():
    df1 = pd.read_csv("../../data/etf_cape_return_forecast.csv")
    df2 = pd.read_csv("../../data/stock_cape_return_forecast.csv")
    df3 = pd.read_csv("../../data/acf_yield.csv")
    df4 = pd.concat([
        pd.read_csv("../../data/outlier_etf_cape_forecast.csv"),
        pd.read_csv("../../data/outlier_stock_cape_forecast.csv")
    ])

    df1['SECURITY_TYPE'] = 'Equity ETF'
    df2['SECURITY_TYPE'] = 'Common Stock'
    df3['SECURITY_TYPE'] = 'Bond ETF'
    # df4['OUTLIER_BOOL'] = True

    df = pd.concat([df1, df2, df3], ignore_index=True)

    for ticker in df.TICKER.values:
        if ticker in df4.TICKER.values:
            df['OUTLIER_BOOL'] = True
        else:
            df['OUTLIER_BOOL'] = False

    df['CAPE'] = df['CAPE'].map('{:,.2f}'.format)
    df['FWD_RETURN_FORECAST'] = df['FWD_RETURN_FORECAST'].map('{:,.2%}'.format)
    df['LOWER_CONFIDENCE'] = df['LOWER_CONFIDENCE'].map('{:,.2%}'.format)
    df['UPPER_CONFIDENCE'] = df['UPPER_CONFIDENCE'].map('{:,.2%}'.format)
    df['F_PVALUE'] = df['F_PVALUE'].map('{:,.4f}'.format)
    df['ACF_YIELD'] = df['ACF_YIELD'].map('{:,.2%}'.format)
    df['VOLATILITY_162W'] = df['VOLATILITY_162W'].map('{:,.2%}'.format)
    df['YLD_VOL_RATIO'] = df['YLD_VOL_RATIO'].map('{:,.2f}'.format)
    df['PE_RATIO'] = df['PE_RATIO'].map('{:,.2f}'.format)

    tickers = df.TICKER.tolist()

    # Delete records from the database that are not in the list of tickers
    Forecast.objects.exclude(ticker__in=tickers).delete()

    # Iterate over the rows of the concatenated dataframe
    for index, row in tqdm(df.iterrows()):
        # set the ticker by security type
        if row.SECURITY_TYPE == 'Equity ETF':
            ticker = row.INDEX_TICKER
        else:
            ticker = row.TICKER
        # Check if a record with the same ticker already exists in the database
        if Forecast.objects.filter(ticker=row.TICKER).exists():
            # Update the existing record
            obj = Forecast.objects.get(ticker=row.TICKER)
            obj.ticker = row.TICKER
            obj.name = row.NAME
            obj.index_name = row.INDEX_NAME
            obj.cape = row.CAPE
            obj.fwd_return_forecast = row.FWD_RETURN_FORECAST
            obj.lower_confidence = row.LOWER_CONFIDENCE
            obj.upper_confidence = row.UPPER_CONFIDENCE
            obj.f_pvalue = row.F_PVALUE
            obj.index_ticker = row.INDEX_TICKER
            obj.security_type = row.SECURITY_TYPE
            obj.acf_yield = row.ACF_YIELD
            obj.volatility_162W = row.VOLATILITY_162W
            obj.yield_vol_ratio = row.YLD_VOL_RATIO
            obj.bond_pe_ratio = row.PE_RATIO
            obj.outlier_bool = row.OUTLIER_BOOL
            obj.expected_fwd_return_chart = 'expected_fwd_return_{}.jpg'.format(ticker)
            obj.long_term_pe_ratio_chart = 'long_term_pe_ratio_{}.jpg'.format(ticker)
            obj.sample_observed_forecast_chart = 'sample_observed_forecast_{}.jpg'.format(ticker)
            obj.sample_regression_chart = 'sample_regression_{}.jpg'.format(ticker)
            # add the fields according to the model structure
            obj.save()
        else:
            # Create a new record
            obj = Forecast(
                ticker=row.TICKER,
                name=row.NAME,
                index_name=row.INDEX_NAME,
                cape=row.CAPE,
                fwd_return_forecast=row.FWD_RETURN_FORECAST,
                lower_confidence=row.LOWER_CONFIDENCE,
                upper_confidence=row.UPPER_CONFIDENCE,
                f_pvalue=row.F_PVALUE,
                index_ticker=row.INDEX_TICKER,
                security_type=row.SECURITY_TYPE,
                acf_yield=row.ACF_YIELD,
                volatility_162W=row.VOLATILITY_162W,
                yield_vol_ratio=row.YLD_VOL_RATIO,
                bond_pe_ratio=row.PE_RATIO,
                outlier_bool=row.OUTLIER_BOOL,
                expected_fwd_return_chart='expected_fwd_return_{}.jpg'.format(ticker),
                long_term_pe_ratio_chart='long_term_pe_ratio_{}.jpg'.format(ticker),
                sample_observed_forecast_chart='sample_observed_forecast_{}.jpg'.format(ticker),
                sample_regression_chart='sample_regression_{}.jpg'.format(ticker),
            )
            # add the fields according to the model structure
            obj.save()


if __name__ == '__main__':
    run()
