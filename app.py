import streamlit as st
import pandas as pd
import pickle
import plotly.express as px

st.title("Piramal Pharma Stock Forecast Dashboard")

# load historical data
hist = pd.read_csv("PPLPHARMA.csv")

# load forecast data
forecast = pd.read_csv("PPLPHARMA_future_forecast (2).csv")

# load model
with open("forecast_model.pkl","rb") as f:
    model = pickle.load(f)

st.subheader("Historical Data")
st.dataframe(hist.tail())

st.subheader("Forecast Data")
st.dataframe(forecast)

fig = px.line(forecast, x="ds", y="yhat",
              title="Forecasted Price Trend")

st.plotly_chart(fig)
# Load CSS
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

st.set_page_config(page_title="Piramal Finance Forecast", layout="wide")

# Logos
col1, col2 = st.columns([1,6])

with col1:
    st.image("piramal_logo.png", width=120)

with col2:
    st.image("college_logo.png", width=120)

# Title
st.markdown('<div class="title">Piramal Finance Stock Forecast Dashboard</div>', unsafe_allow_html=True)

st.markdown('<div class="subtitle">AI Based Time Series Forecasting Model</div>', unsafe_allow_html=True)

# Load forecast data
forecast = pd.read_csv("forecast_data.csv")

# Graph section
st.markdown('<div class="section-header">Forecast Trend</div>', unsafe_allow_html=True)

fig = px.line(forecast, x="ds", y="yhat", title="Forecasted Price")

st.plotly_chart(fig, use_container_width=True)

# Table
st.markdown('<div class="section-header">Forecast Table</div>', unsafe_allow_html=True)

st.dataframe(forecast)

# Submitted by section
st.markdown("""
<div class="submitted-box">
<div class="submitted-title">Submitted By</div>
<div class="student-text">
Name: Dhinagaran Ravichnahdiran <br>
Course: MBA Financial Markets <br>
Project: Stock Price Forecasting Using Machine Learning <br>
Company: Piramal Finance
</div>
</div>
""", unsafe_allow_html=True)
