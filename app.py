import streamlit as st
import pandas as pd

st.title('😴 Sleep Score Prediction APP')

st.info('This is developed by using the Machine Learning Algorithm🤖')

with st.expander('Data'):
  st.write('**Raw Data**')
  ds = pd.read_csv('https://raw.githubusercontent.com/Ragulvasan08/Sleep_Score_Prediction/refs/heads/main/Sleep_Quality.csv')
  ds.drop(columns=['Movement_During_Sleep','Stress_Level'], axis=1, inplace = True)
  ds

  st.write('**X**')
  X = ds.drop('Sleep_Quality_Score', axis=1)
  X

  st.write('**Y**')
  Y = ds.Sleep_Quality_Score
  Y

with st.expander('Data Visualization'):
  st.area_chart(data=ds, x='Heart_Rate_Variability', y='Body_Temperature', color='Sleep_Quality_Score', use_container_width=True)

#Data Preparation
with st.sidebar:
  st.header('Input Features')
  #Heart_Rate_Variability,Body_Temperature, Sleep_Duration_Hours, Caffeine_Intake_mg,Bedtime_Consistency,Light_Exposure_hours
  Heart_Rate_Variability = st.slider("Enter your Heart Rate Variability (ms)", 0.0, 100.0, 50.0, step=0.1)
  Body_Temperature = st.slider("Enter your Body Temperature (°C)", 0.0, 100.0, 36.5, step=0.1)
  Sleep_Duration_Hours = st.slider("Enter your Sleep Duration (hrs)", 0.0, 12.0, 8.0, step=0.1)
  Caffeine_Intake_mg = st.slider("Enter your Caffeine Intake (mg)", 0.0, 500.0, 100.0, step=1.0)
  Bedtime_Consistency = st.slider("Enter your Bedtime Consistency (hrs)", 0.0, 10.0, 1.0, step=0.1)
  Light_Exposure_hours = st.slider("Enter your Light Exposure (hrs)", 0.0, 24.0, 5.0, step=0.1)
  
  



