import streamlit as st
import pandas as pd

st.title('😴 Sleep Score Prediction APP')

st.info('This is developed by using the Machine Learning Algorithm🤖')

with st.expander('Data'):
  st.write('**Raw Data**')
  data = pd.read_csv('https://raw.githubusercontent.com/Ragulvasan08/Sleep_Score_Prediction/refs/heads/main/Sleep_Quality.csv')
  data




