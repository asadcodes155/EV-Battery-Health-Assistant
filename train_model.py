import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib  
from sklearn.model_selection import train_test_split


#read csv

df = pd.read_csv("data/ev_battery_charging_data.csv")

#dropping null values
print(df.isnull().sum())
df.dropna()


#assigning columns to x & y
features = [
    "SOC (%)",
    "Voltage (V)",
    "Current (A)",
    "Battery Temp (°C)",
    "Ambient Temp (°C)",
    "Charging Duration (min)",
    "Efficiency (%)",
    "Charging Cycles"
]
x= df[features]
y = df['Degradation Rate (%)'] 
#splitting the data into train and test

x_train , x_test , y_train , y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)


#setting up model

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(x_train,y_train)

joblib.dump(model,'data/ml_model.pk1')