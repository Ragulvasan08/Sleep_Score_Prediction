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
  Heart_Rate_Variability = st.number_input(
    "Enter your Heart_Rate_Variability", value=None, placeholder="Type a number..."
  )
  Body_Temperature = st.number_input(
    "Enter your Body_Temperature", value=None, placeholder="Type a number..."
  )
  Sleep_Duration_Hours = st.number_input(
    "Enter your Sleep_Duration_Hours", value=None, placeholder="Type a number..."
  )
  Caffeine_Intake_mg = st.number_input(
    "Enter your Caffeine_Intake_mg", value=None, placeholder="Type a number..."
  )
  Bedtime_Consistency = st.number_input(
    "Enter your Bedtime_Consistency", value=None, placeholder="Type a number..."
  )
  Light_Exposure_hours = st.number_input(
    "Enter your Light_Exposure_hours", value=None, placeholder="Type a number..."
  )
  
  



