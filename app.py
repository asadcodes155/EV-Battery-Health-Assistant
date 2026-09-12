import streamlit as st
import pandas as pd
import joblib


st.title('Hello')
#page config

st.set_page_config(
    page_title='EV Battery Health Assistant',
    page_icon = "🔋",
    layout = 'wide'
)

#loading model
model = joblib.load('data/ml_model.pk1')

#setting up the title

st.title("🔋 EV Battery Health Assistant")
st.write( 
    """
    Upload an EV battery log (CSV) to analyse battery health.
    """
    )

#upload file

file_upload= st.file_uploader(
    label = 'Upload Here!',
    type = 'csv'
)

if file_upload is not None:
  df = pd.read_csv(file_upload)
  st.success('File uploaded succesfully')

  st.subheader('Battery log')
  st.dataframe(df, use_container_width=True)

  #removing null values
  df.dropna()

  # Battery Analysis
  avg_voltage = df["Voltage (V)"].mean()
  avg_temperature = df["Battery Temp (°C)"].mean()
  avg_current = df["Current (A)"].mean()
  avg_charge_cycle = df["Charging Cycles"].mean()
  fast_charge_percentage = (
     (df['Charging Mode']=='Fast').mean() * 100
     ) 
  avg_soc = df["SOC (%)"].mean()
  avg_ambient_temp = df["Ambient Temp (°C)"].mean()
  avg_charging_duration = df["Charging Duration (min)"].mean()
  avg_efficiency = df["Efficiency (%)"].mean()

# Prepare Input for ML Model
  input_data = pd.DataFrame({
    "SOC (%)": [avg_soc],
    "Voltage (V)": [avg_voltage],
    "Current (A)": [avg_current],
    "Battery Temp (°C)": [avg_temperature],
    "Ambient Temp (°C)": [avg_ambient_temp],
    "Charging Duration (min)": [avg_charging_duration],
    "Efficiency (%)": [avg_efficiency],
    "Charging Cycles": [avg_charge_cycle]
})
# Predict Degradation Rate 
  predicted_degradation = model.predict(input_data)[0]


# Battery Metrics
  st.subheader("Battery Summary")

  col1, col2, col3, col4, col5, col6 = st.columns(6)

  col1.metric(
        "Average Voltage",
        f"{avg_voltage:.2f} V"
    )

  col2.metric(
        "Average Temperature",
        f"{avg_temperature:.1f} °C"
    )

  col3.metric(
        "Average Current",
        f"{avg_current:.1f} A"
    )

  col4.metric(
        "Average Charge Cycles",
        int(avg_charge_cycle)
    )

  col5.metric(
        "Fast Charging",
        f"{fast_charge_percentage:.0f}%"
    )
  col6.metric(
    "Predicted Degradation",
    f"{predicted_degradation:.2f}%"
)

else: 
   st.info('Please upload a CSV file to begin.')