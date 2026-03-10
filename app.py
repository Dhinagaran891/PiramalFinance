from prophet import Prophet
import pandas as pd
import joblib

# Load dataset
df = pd.read_csv("piramal_data.csv")

# Train model
model = Prophet()
model.fit(df)

# Save the model
joblib.dump(model, "forecast_model.pkl")

print("Model saved successfully")
