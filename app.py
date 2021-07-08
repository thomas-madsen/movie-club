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
An interactive recommender of *new* movies which all members are likely to enjoy.
Data from Letterboxd and MovieLens. Powered by Streamlit and Heroku.
"""

st.sidebar.header("Tell us about your group:")
members = range(2,10)
members_option = st.sidebar.selectbox('Number of Watchers:', members, index=1)

st.subheader("List a few of your favorite movies!")
cols = st.beta_columns(members_option)

movie_1_1 = cols[0].text_input("Watcher 1","")
cols[1].text_input("Watcher 2","")
cols[2].text_input("Watcher 3","")

for i in range(0,4):
    cols[0].text_input("", "", key = "watcher1movie"+str(i))
    cols[1].text_input("", "", key = "watcher2movie"+str(i))
    cols[2].text_input("", "", key = "watcher3movie"+str(i))

if movie_1_1 == "Toy Story":
    st.subheader("Our suggestions:")
    st.write("[The Mitchells vs. The Machines (2021)](https://letterboxd.com/film/the-mitchells-vs-the-machines/)")
    st.write("[Soul (2020)](https://letterboxd.com/film/soul-2020/)")
    st.write("[Onward (2020)](https://letterboxd.com/film/onward-2020/)")
    st.write("[Nomadland (2020)](https://letterboxd.com/film/nomadland/)")
    st.write("[Anomalisa (2015)](https://letterboxd.com/film/anomalisa/)")

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