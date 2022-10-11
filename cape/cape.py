import pandas as pd
from IPython.display import Image


def print_data_date():
    print('Data current as of: {}'.format(
        pd.read_csv('https://raw.githubusercontent.com/nathanramoscfa/cape/main/data/as_of_date.csv'
                    ).iloc[:, 1:].squeeze()))


def forecast_data():
    df = pd.read_csv(
        'https://raw.githubusercontent.com/nathanramoscfa/cape/main/data/cape_return_forecast.csv', index_col=0)
    df.index.name = 'TICKER'
    return df


def import_results():
    print('Data current as of: {}'.format(
        pd.read_csv('https://raw.githubusercontent.com/nathanramoscfa/cape/main/data/as_of_date.csv'
                    ).iloc[:, 1:].squeeze()))
    df = pd.read_csv(
        'https://raw.githubusercontent.com/nathanramoscfa/cape/main/data/cape_return_forecast.csv', index_col=0)
    df.index.name = 'TICKER'
    return df


def forward_return_forecast(breakpoint_return=0.10, above=True, top=None, drop_duplicates=False):
    fwd_return_5y_forecast = forecast_data()
    if above:
        print('ETFs with above {}% expected forward 5-year return:'.format(breakpoint_return))
        if drop_duplicates:
            df = fwd_return_5y_forecast[
                     fwd_return_5y_forecast.FWD_RETURN_5Y_FORECAST >= breakpoint_return].sort_values(
                by='FWD_RETURN_5Y_FORECAST', ascending=False).drop_duplicates(subset=['INDEX_TICKER']).iloc[:top, :]
        else:
            df = fwd_return_5y_forecast[
                     fwd_return_5y_forecast.FWD_RETURN_5Y_FORECAST >= breakpoint_return].sort_values(
                by='FWD_RETURN_5Y_FORECAST', ascending=False).iloc[:top, :]
    else:
        print('ETFs with below {}% expected forward 5-year return:'.format(breakpoint_return))
        if drop_duplicates:
            df = fwd_return_5y_forecast[
                     fwd_return_5y_forecast.FWD_RETURN_5Y_FORECAST <= breakpoint_return].sort_values(
                by='FWD_RETURN_5Y_FORECAST').drop_duplicates(subset=['INDEX_TICKER']).iloc[:top, :]
        else:
            df = fwd_return_5y_forecast[
                     fwd_return_5y_forecast.FWD_RETURN_5Y_FORECAST <= breakpoint_return].sort_values(
                by='FWD_RETURN_5Y_FORECAST').iloc[:top, :]
    return df


def available_tickers():
    fwd_return_5y_forecast = forecast_data()
    print('Available ETF tickers: \n')
    for x in range(0, len(list(fwd_return_5y_forecast.sort_index().index)), 10):
        print(*list(fwd_return_5y_forecast.sort_index().index)[x:x + 10])


def check_ticker(etf_ticker):
    fwd_return_5y_forecast = forecast_data()
    if etf_ticker not in fwd_return_5y_forecast.index:
        print('Available ETF tickers: \n')
        for x in range(0, len(list(fwd_return_5y_forecast.sort_index().index)), 10):
            print(*list(fwd_return_5y_forecast.sort_index().index)[x:x + 10])
        raise IndexError('The etf_ticker is not available in the results. Please input a valid etf_ticker.')


def ticker_results(etf_ticker):
    try:
        fwd_return_5y_forecast = forecast_data()
        print(fwd_return_5y_forecast.loc[etf_ticker])
        print('Expected 5-Year Return ({}): {}%'.format(fwd_return_5y_forecast.loc[etf_ticker].loc['INDEX_NAME'], round(
            fwd_return_5y_forecast.loc[etf_ticker].loc['FWD_RETURN_5Y_FORECAST'] * 100, 2)))
    except KeyError:
        check_ticker()


def chart(etf_ticker, chart_num=1):
    fwd_return_5y_forecast = forecast_data()
    index_ticker = fwd_return_5y_forecast.loc[etf_ticker]['INDEX_TICKER']
    if chart_num == 1:
        Image(
            'https://raw.githubusercontent.com/nathanramoscfa/cape/main/charts/sample_regression_{}.png'.format(
                index_ticker))
    elif chart_num == 2:
        Image(
            'https://raw.githubusercontent.com/nathanramoscfa/cape/main/charts/sample_regression_heatmap_{}.png'.format(
                index_ticker))
    elif chart_num == 3:
        Image(
            'https://raw.githubusercontent.com/nathanramoscfa/cape/main/charts/sample_observed_forecast_{}.png'.format(
                index_ticker))
    elif chart_num == 4:
        Image('https://raw.githubusercontent.com/nathanramoscfa/cape/main/charts/long_term_pe_ratio_{}.png'.format(
            index_ticker))
    elif chart_num == 5:
        Image('https://raw.githubusercontent.com/nathanramoscfa/cape/main/charts/expected_fwd_return_5y_{}.png'.format(
            index_ticker))
    else:
        raise ValueError('Invalid chart_num parameter. Must input integer from 1 to 5 corresponding to desired chart.')
