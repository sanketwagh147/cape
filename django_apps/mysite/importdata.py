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
    print('reading csv...')
    etf_cape_df = pd.read_csv("../../data/etf_cape_return_forecast.csv")
    etf_cape_df.CAPE = etf_cape_df.CAPE.map('{:,.2f}'.format)
    etf_cape_df.FWD_RETURN_FORECAST = etf_cape_df.FWD_RETURN_FORECAST.map('{:,.2%}'.format)
    etf_cape_df.LOWER_CONFIDENCE = etf_cape_df.LOWER_CONFIDENCE.map('{:,.2%}'.format)
    etf_cape_df.UPPER_CONFIDENCE = etf_cape_df.UPPER_CONFIDENCE.map('{:,.2%}'.format)
    etf_cape_df.F_PVALUE = etf_cape_df.F_PVALUE.map('{:,.4f}'.format)
    array = etf_cape_df.to_dict(orient='records')
    entries = Forecast.objects.values_list('ticker')
    entries = [entry[0] for entry in entries]
    for entry in tqdm(array):
        if entry['TICKER'] not in entries:
            forecast = Forecast(
                ticker=entry['TICKER'],
                name=entry['NAME'],
                index_name=entry['INDEX_NAME'],
                cape=entry['CAPE'],
                fwd_return_forecast=entry['FWD_RETURN_FORECAST'],
                lower_confidence=entry['LOWER_CONFIDENCE'],
                upper_confidence=entry['UPPER_CONFIDENCE'],
                f_pvalue=entry['F_PVALUE'],
                index_ticker=entry['INDEX_TICKER'],
                expected_fwd_return_chart='expected_fwd_return_{}.jpg'.format(entry['INDEX_TICKER']),
                long_term_pe_ratio_chart='long_term_pe_ratio_{}.jpg'.format(entry['INDEX_TICKER']),
                sample_observed_forecast_chart='sample_observed_forecast_{}.jpg'.format(entry['INDEX_TICKER']),
                sample_regression_chart='sample_regression_{}.jpg'.format(entry['INDEX_TICKER']),
                security_type='Equity ETF'
            )
            forecast.save()
        else:
            forecast = Forecast.objects.get(ticker=entry['TICKER'])
            forecast.name = etf_cape_df[etf_cape_df['TICKER'] == entry['TICKER']].NAME.iloc[0]
            forecast.index_name = etf_cape_df[etf_cape_df['TICKER'] == entry['TICKER']].INDEX_NAME.iloc[0]
            forecast.cape = etf_cape_df[etf_cape_df['TICKER'] == entry['TICKER']].CAPE.iloc[0]
            forecast.fwd_return_forecast = etf_cape_df[etf_cape_df['TICKER'] == entry['TICKER']].FWD_RETURN_FORECAST.iloc[0]
            forecast.lower_confidence = etf_cape_df[etf_cape_df['TICKER'] == entry['TICKER']].LOWER_CONFIDENCE.iloc[0]
            forecast.upper_confidence = etf_cape_df[etf_cape_df['TICKER'] == entry['TICKER']].UPPER_CONFIDENCE.iloc[0]
            forecast.f_pvalue = etf_cape_df[etf_cape_df['TICKER'] == entry['TICKER']].F_PVALUE.iloc[0]
            forecast.index_ticker = etf_cape_df[etf_cape_df['TICKER'] == entry['TICKER']].INDEX_TICKER.iloc[0]
            forecast.expected_fwd_return_chart = 'expected_fwd_return_{}.jpg'.format(
                etf_cape_df[etf_cape_df['TICKER'] == entry['TICKER']].INDEX_TICKER.iloc[0])
            forecast.long_term_pe_ratio_chart = 'long_term_pe_ratio_{}.jpg'.format(
                etf_cape_df[etf_cape_df['TICKER'] == entry['TICKER']].INDEX_TICKER.iloc[0])
            forecast.sample_observed_forecast_chart = 'sample_observed_forecast_{}.jpg'.format(
                etf_cape_df[etf_cape_df['TICKER'] == entry['TICKER']].INDEX_TICKER.iloc[0])
            forecast.sample_regression_chart = 'sample_regression_{}.jpg'.format(
                etf_cape_df[etf_cape_df['TICKER'] == entry['TICKER']].INDEX_TICKER.iloc[0])
            forecast.security_type = 'Equity ETF'
            forecast.save()

    stock_cape_df = pd.read_csv("../../data/stock_cape_return_forecast.csv")
    stock_cape_df.CAPE = stock_cape_df.CAPE.map('{:,.2f}'.format)
    stock_cape_df.FWD_RETURN_FORECAST = stock_cape_df.FWD_RETURN_FORECAST.map('{:,.2%}'.format)
    stock_cape_df.LOWER_CONFIDENCE = stock_cape_df.LOWER_CONFIDENCE.map('{:,.2%}'.format)
    stock_cape_df.UPPER_CONFIDENCE = stock_cape_df.UPPER_CONFIDENCE.map('{:,.2%}'.format)
    stock_cape_df.F_PVALUE = stock_cape_df.F_PVALUE.map('{:,.4f}'.format)
    array = stock_cape_df.to_dict(orient='records')
    entries = [entry[0] for entry in Forecast.objects.values_list('ticker')]
    for entry in tqdm(array):
        if entry['TICKER'] not in entries:
            forecast = Forecast(
                ticker=entry['TICKER'],
                name=entry['NAME'],
                cape=entry['CAPE'],
                fwd_return_forecast=entry['FWD_RETURN_FORECAST'],
                lower_confidence=entry['LOWER_CONFIDENCE'],
                upper_confidence=entry['UPPER_CONFIDENCE'],
                f_pvalue=entry['F_PVALUE'],
                expected_fwd_return_chart='expected_fwd_return_{}.jpg'.format(entry['TICKER']),
                long_term_pe_ratio_chart='long_term_pe_ratio_{}.jpg'.format(entry['TICKER']),
                sample_observed_forecast_chart='sample_observed_forecast_{}.jpg'.format(entry['TICKER']),
                sample_regression_chart='sample_regression_{}.jpg'.format(entry['TICKER']),
                security_type='Common Stock'
            )
            forecast.save()
        else:
            forecast = Forecast.objects.get(ticker=entry['TICKER'])
            forecast.name = stock_cape_df[stock_cape_df['TICKER'] == entry['TICKER']].NAME.iloc[0]
            forecast.cape = stock_cape_df[stock_cape_df['TICKER'] == entry['TICKER']].CAPE.iloc[0]
            forecast.fwd_return_forecast = stock_cape_df[stock_cape_df['TICKER'] == entry['TICKER']].FWD_RETURN_FORECAST.iloc[0]
            forecast.lower_confidence = stock_cape_df[stock_cape_df['TICKER'] == entry['TICKER']].LOWER_CONFIDENCE.iloc[0]
            forecast.upper_confidence = stock_cape_df[stock_cape_df['TICKER'] == entry['TICKER']].UPPER_CONFIDENCE.iloc[0]
            forecast.f_pvalue = stock_cape_df[stock_cape_df['TICKER'] == entry['TICKER']].F_PVALUE.iloc[0]
            forecast.expected_fwd_return_chart = 'expected_fwd_return_{}.jpg'.format(
                stock_cape_df[stock_cape_df['TICKER'] == entry['TICKER']].TICKER.iloc[0])
            forecast.long_term_pe_ratio_chart = 'long_term_pe_ratio_{}.jpg'.format(
                stock_cape_df[stock_cape_df['TICKER'] == entry['TICKER']].TICKER.iloc[0])
            forecast.sample_observed_forecast_chart = 'sample_observed_forecast_{}.jpg'.format(
                stock_cape_df[stock_cape_df['TICKER'] == entry['TICKER']].TICKER.iloc[0])
            forecast.sample_regression_chart = 'sample_regression_{}.jpg'.format(
                stock_cape_df[stock_cape_df['TICKER'] == entry['TICKER']].TICKER.iloc[0])
            forecast.security_type = 'Common Stock'
            forecast.save()

    bond_etf_df = pd.read_csv("../../data/acf_yield.csv")
    bond_etf_df.ACF_YIELD = bond_etf_df.ACF_YIELD.map('{:,.2%}'.format)
    bond_etf_df.VOLATILITY_162W = bond_etf_df.VOLATILITY_162W.map('{:,.2%}'.format)
    bond_etf_df.YLD_VOL_RATIO = bond_etf_df.YLD_VOL_RATIO.map('{:,.2f}'.format)
    array = bond_etf_df.to_dict(orient='records')
    entries = [entry[0] for entry in Forecast.objects.values_list('ticker')]
    for entry in tqdm(array):
        if entry['TICKER'] not in entries:
            forecast = Forecast(
                ticker=entry['TICKER'],
                name=entry['NAME'],
                acf_yield=entry['ACF_YIELD'],
                volatility_162W=entry['VOLATILITY_162W'],
                yield_vol_ratio=entry['YLD_VOL_RATIO'],
                bond_pe_ratio=entry['PE_RATIO'],
                security_type='Bond ETF'
            )
            forecast.save()
        else:
            forecast = Forecast.objects.get(ticker=entry['TICKER'])
            forecast.name = bond_etf_df[bond_etf_df['TICKER'] == entry['TICKER']].NAME.iloc[0]
            forecast.acf_yield = bond_etf_df[bond_etf_df['TICKER'] == entry['TICKER']].ACF_YIELD.iloc[0]
            forecast.volatility_162W = bond_etf_df[bond_etf_df['TICKER'] == entry['TICKER']].VOLATILITY_162W.iloc[0]
            forecast.yield_vol_ratio = bond_etf_df[bond_etf_df['TICKER'] == entry['TICKER']].YLD_VOL_RATIO.iloc[0]
            forecast.bond_pe_ratio = bond_etf_df[bond_etf_df['TICKER'] == entry['TICKER']].PE_RATIO.iloc[0]
            forecast.security_type = 'Bond ETF'
            forecast.save()
    print('Saved all entries to database.')
    return


if __name__ == "__main__":
    run()
