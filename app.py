import streamlit as st
import pandas as pd

st.title('😴 Sleep Score Prediction APP')

st.info('This is developed by using the Machine Learning Algorithm🤖')

with st.expander('Data'):
  st.write('**Raw Data**')
  ds = pd.read_csv('https://raw.githubusercontent.com/Ragulvasan08/Sleep_Score_Prediction/refs/heads/main/Sleep_Quality.csv')
  ds

  st.write('**X**')
  X = ds.drop('Sleep_Quality_Score', axis=1)
  X

  st.write('**Y**')
  Y = ds.Sleep_Quality_Score
  Y

with st.expander('Data Visualization'):
st.write('**Line Chart of Sleep Quality vs Other Features**')
# Example: Line chart for Sleep Duration and Sleep Quality
st.line_chart(data=ds[['Sleep_Duration_Hours', 'Sleep_Quality_Score']])  # Visualize Sleep Duration and Quality
# You can add more charts as needed
# Example for Heart Rate Variability and Sleep Quality Score
st.line_chart(data=ds[['Heart_Rate_Variability', 'Sleep_Quality_Score']])
# Example for Caffeine Intake and Sleep Quality Score
st.line_chart(data=ds[['Caffeine_Intake_mg', 'Sleep_Quality_Score']])

  




