# EV-Battery-Health-Assistant
🔋 EV Battery Health Assistant

An ML-powered Streamlit application that analyzes electric vehicle battery logs and predicts battery degradation based on key battery and charging characteristics.

📌 Overview

The EV Battery Health Assistant allows users to upload an EV battery log in CSV format and receive a quick summary of important battery metrics along with a machine-learning prediction of the battery's degradation rate.

The application combines Python, Pandas, Scikit-learn/joblib, and Streamlit to turn raw battery data into an easy-to-understand dashboard.

✨ Features
📂 Upload EV battery logs in CSV format
📊 Display the uploaded battery data
🔋 Calculate average battery voltage
🌡️ Calculate average battery temperature
⚡ Calculate average current
🔄 Calculate average charging cycles
🚀 Calculate the percentage of fast charging sessions
🤖 Predict battery degradation using a trained ML model
📈 Display battery metrics through an interactive Streamlit interface
🧠 How It Works

The application follows a simple machine-learning pipeline:

EV Battery CSV
      ↓
Upload Dataset
      ↓
Read & Process Data
      ↓
Calculate Battery Metrics
      ↓
Prepare Features for ML Model
      ↓
Trained ML Model
      ↓
Predicted Battery Degradation
      ↓
Display Results

The application calculates average values from the uploaded battery log and uses these values as input features for the trained machine-learning model.

📊 Input Features

The ML model uses the following battery characteristics:

Feature	Description
SOC (%)	State of Charge
Voltage (V)	Battery voltage
Current (A)	Battery current
Battery Temp (°C)	Battery temperature
Ambient Temp (°C)	Surrounding temperature
Charging Duration (min)	Charging duration
Efficiency (%)	Charging efficiency
Charging Cycles	Number of charging cycles

The uploaded CSV should contain these columns for the prediction to work correctly.

🛠️ Technologies Used
Python
Streamlit — interactive web application
Pandas — data processing and analysis
Joblib — loading the trained machine-learning model
Machine Learning — battery degradation prediction
