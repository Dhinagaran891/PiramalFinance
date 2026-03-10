import streamlit as st
import pandas as pd
import pickle
import plotly.express as px

# Page configuration (must be first)
st.set_page_config(page_title="Piramal Finance Forecast", layout="wide")

# Load CSS
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Logos at top
col1, col2 = st.columns(2)

with col1:
    st.image("piramal_logo.png", width=120)

with col2:
    st.image("college_logo.png", width=120)

# Title
st.markdown('<div class="title">Piramal Finance Stock Forecast Dashboard</div>', unsafe_allow_html=True)

st.markdown('<div class="subtitle">AI Based Time Series Forecasting Model</div>', unsafe_allow_html=True)

# Load data
hist = pd.read_csv("PPLPHARMA.csv")
forecast = pd.read_csv("PPLPHARMA_future_forecast (2).csv")

# Load model
with open("forecast_model.pkl","rb") as f:
    model = pickle.load(f)

# Historical Data
st.markdown('<div class="section-header">Historical Data</div>', unsafe_allow_html=True)
st.dataframe(hist.tail())

# Forecast Graph
st.markdown('<div class="section-header">Forecast Trend</div>', unsafe_allow_html=True)

fig = px.line(
    forecast,
    x="ds",
    y="yhat",
    title="Forecasted Price Trend"
)

st.plotly_chart(fig, use_container_width=True)

# Forecast Table
st.markdown('<div class="section-header">Forecast Table</div>', unsafe_allow_html=True)
st.dataframe(forecast)

# Prepared By section (clean professional style)
st.markdown("""
<div class="submitted-section">

<div class="submitted-title">Prepared By</div>

<div class="student-text">
Name: Dhinagaran R <br>
Department: MBA <br>
The Kavery Engineering College, Salem <br>
Project: Stock Price Forecasting Using Machine Learning <br>
Company: Piramal Finance
</div>

</div>
""", unsafe_allow_html=True)
