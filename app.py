import streamlit as st
import numpy as np
import pandas as pd
import requests
import json
import simplejson
import plotly.express as px
import datetime
import os

"""
# Movie Club Recommender
An interactive app for movie clubs. Recommends *new* movies which all members are likely to enjoy.
"""

years = np.arange(2010,2022,1)
months = np.arange(1,13,1)
st.sidebar.header("Select plot parameters:")

ticker = st.sidebar.text_input(
    'Ticker (e.g. AAPL):',
    'AAPL')

year_option = st.sidebar.selectbox(
    'Year:',
    years)

month_option = st.sidebar.selectbox(
    'Month:',
    months)

st.text_area("Watcher #1", "")

#key = os.environ.get('key')
#url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&outputsize=full&symbol={}&apikey={}'.format(ticker, key)
#response_json = requests.get(url).json()

#time_series_df = pd.DataFrame(response_json['Time Series (Daily)'])
#df = pd.DataFrame({'price': time_series_df.loc['5. adjusted close'].astype('float'),'date': pd.to_datetime(time_series_df.columns)})

#from pandas.tseries.offsets import MonthEnd
#start_date = pd.to_datetime('{}-{}-01'.format(year_option, month_option))
#end_date = start_date + MonthEnd(1)

#filtered_df = df.loc[(df['date'] >= start_date) & (df['date'] < end_date)]

#fig = px.line(filtered_df, x='date', y='price')

#fig.update_layout(title='{} Closing Price, {}/{}'.format(ticker, month_option, year_option),
#                   xaxis_title='Date',
#                   yaxis_title='(Adjusted) Closing Price (USD)',
#                   showlegend=False)

#st.plotly_chart(fig)