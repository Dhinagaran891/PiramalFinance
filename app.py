import streamlit as st
import pandas as pd
import pickle
import plotly.express as px

st.title("Piramal Pharma Stock Forecast Dashboard")

# load historical data
hist = pd.read_csv("PPLPHARMA.csv")

# load forecast data
forecast = pd.read_csv("PPLPHARMA_future_forecast(2).csv")

# load model
with open("forecast_model.pkl","rb") as f:
    model = pickle.load(f)

st.subheader("Historical Data")
st.dataframe(hist.tail())

st.subheader("Forecast Data")
st.dataframe(forecast)

fig = px.line(forecast, x="Date", y="Predicted_Price",
              title="Forecasted Price Trend")

st.plotly_chart(fig)
