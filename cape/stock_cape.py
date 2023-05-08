import pandas as pd
from IPython.display import Image, display


def print_data_date():
    print('Data current as of: {}'.format(
        pd.read_csv('../data/stock_cape_as_of_date.csv'
                    ).iloc[:, 1:].squeeze()))


def forecast_data():
    df = pd.read_csv(
        '../data/stock_cape_return_forecast.csv', index_col=0)
    df.index.name = 'TICKER'
    return df


def import_results():
    print('Data current as of: {}'.format(
        pd.read_csv('../data/stock_cape_as_of_date.csv'
                    ).iloc[:, 1:].squeeze()))
    df = pd.read_csv(
        '../data/stock_cape_return_forecast.csv', index_col=0)
    df.index.name = 'TICKER'
    return df


def forward_return_forecast(breakpoint_return=0.10, above=True, top=None, drop_duplicates=False):
    fwd_return_forecast = forecast_data()
    if above:
        print('ETFs with above {}% expected forward return:'.format(breakpoint_return*100))
        if drop_duplicates:
            df = fwd_return_forecast[
                     fwd_return_forecast.FWD_RETURN_FORECAST >= breakpoint_return].sort_values(
                by='FWD_RETURN_FORECAST', ascending=False).drop_duplicates(subset=['INDEX_TICKER']).iloc[:top, :]
        else:
            df = fwd_return_forecast[
                     fwd_return_forecast.FWD_RETURN_FORECAST >= breakpoint_return].sort_values(
                by='FWD_RETURN_FORECAST', ascending=False).iloc[:top, :]
    else:
        print('ETFs with below {}% expected forward return:'.format(breakpoint_return*100))
        if drop_duplicates:
            df = fwd_return_forecast[
                     fwd_return_forecast.FWD_RETURN_FORECAST <= breakpoint_return].sort_values(
                by='FWD_RETURN_FORECAST').drop_duplicates(subset=['INDEX_TICKER']).iloc[:top, :]
        else:
            df = fwd_return_forecast[
                     fwd_return_forecast.FWD_RETURN_FORECAST <= breakpoint_return].sort_values(
                by='FWD_RETURN_FORECAST').iloc[:top, :]
    return df


def available_tickers():
    fwd_return_forecast = forecast_data()
    print('Available ETF tickers: \n')
    for x in range(0, len(list(fwd_return_forecast.sort_index().index)), 10):
        print(*list(fwd_return_forecast.sort_index().index)[x:x + 10])


def check_ticker(etf_ticker):
    fwd_return_forecast = forecast_data()
    if etf_ticker not in fwd_return_forecast.index:
        print('Available ETF tickers: \n')
        for x in range(0, len(list(fwd_return_forecast.sort_index().index)), 10):
            print(*list(fwd_return_forecast.sort_index().index)[x:x + 10])
        raise IndexError('The etf_ticker is not available in the results. Please input a valid etf_ticker.')


def ticker_results(etf_ticker):
    check_ticker(etf_ticker)
    fwd_return_forecast = forecast_data()
    print(fwd_return_forecast.loc[etf_ticker])
    print('Expected Return ({}): {}%'.format(fwd_return_forecast.loc[etf_ticker].loc['INDEX_NAME'], round(
        fwd_return_forecast.loc[etf_ticker].loc['FWD_RETURN_FORECAST'] * 100, 2)))


def chart(etf_ticker, chart_num=1):
    fwd_return_forecast = forecast_data()
    index_ticker = fwd_return_forecast.loc[etf_ticker]['INDEX_TICKER']
    if chart_num == 1:
        display(Image(
            '../django_apps/mysite/forecast/static/forecast/images/sample_regression_{}.jpg'.format(index_ticker)))
    elif chart_num == 2:
        display(Image(
            '../django_apps/mysite/forecast/static/forecast/images/sample_observed_forecast_{}.jpg'.format(index_ticker)))
    elif chart_num == 3:
        display(Image(
            '../main/django_apps/mysite/forecast/static/forecast/images/long_term_pe_ratio_{}.jpg'.format(index_ticker)))
    elif chart_num == 4:
        display(Image(
            '../django_apps/mysite/forecast/static/forecast/images/expected_fwd_return_{}.jpg'.format(index_ticker)))
    else:
        raise ValueError('Invalid chart_num parameter. Must input integer from 1 to 5 corresponding to desired chart.')
