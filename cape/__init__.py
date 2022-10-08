import pandas as pd

print('Data current as of: {}'.format(
    pd.read_csv('https://raw.githubusercontent.com/nathanramoscfa/cape/main/data/as_of_date.csv'
                ).iloc[:, 1:].squeeze()))


fwd_return_5y_forecast = pd.read_csv(
    'https://raw.githubusercontent.com/nathanramoscfa/cape/main/data/cape_return_forecast.csv', index_col=0)
fwd_return_5y_forecast.index.name = 'TICKER'
