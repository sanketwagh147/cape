import streamlit as st
import pandas as pd

df = pd.read_csv('../data/etf_cape_return_forecast.csv')
df = df[['TICKER', 'NAME', 'INDEX_NAME', 'FWD_RETURN_FORECAST', 'LOWER_CONFIDENCE', 'UPPER_CONFIDENCE']]
df = df.sort_values(by='FWD_RETURN_FORECAST', ascending=False)

st.write("Here's our first attempt at using data to create a table:")
st.write(df)
# st.dataframe(df.style.highlight_max(axis=0))
# st.table(df)
