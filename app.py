# import streamlit as st
import pandas as pd
import plotly.express as px

# Title for the App
st.title('😴 Sleep Score Prediction APP')

# Info about the app
st.info('This is developed by using the Machine Learning Algorithm 🤖')

# Load the dataset
ds = pd.read_csv('https://raw.githubusercontent.com/Ragulvasan08/Sleep_Score_Prediction/refs/heads/main/Sleep_Quality.csv')

# Display the data with expander sections
with st.expander('Data'):
    st.write('**Raw Data**')
    st.dataframe(ds)  # Display the raw data

    st.write('**X** (Features)')
    X = ds.drop('Sleep_Quality_Score', axis=1)  # Independent variables (features)
    st.dataframe(X)

    st.write('**Y** (Target)')
    Y = ds['Sleep_Quality_Score']  # Dependent variable (target)
    st.dataframe(Y)

# Data Visualization using Plotly
with st.expander('Data Visualization'):
    st.write('**Line Chart with Colors (Plotly)**')

    # Creating a line chart using Plotly
    fig = px.line(ds, 
                  x=ds.index,  # x-axis as index (or you can specify another column like time)
                  y=['Sleep_Duration_Hours', 'Sleep_Quality_Score'],  # Columns to plot
                  labels={'value': 'Value', 'index': 'Index'},  # Axis labels
                  title='Sleep Duration vs Sleep Quality Score')

    # Customizing lines with different colors
    fig.update_traces(mode='lines+markers')  # Add markers to lines

    # Display the chart in Streamlit
    st.plotly_chart(fig)

    # Another line chart for Heart Rate Variability and Sleep Quality Score
    fig2 = px.line(ds, 
                   x=ds.index, 
                   y=['Heart_Rate_Variability', 'Sleep_Quality_Score'], 
                   labels={'value': 'Value', 'index': 'Index'}, 
                   title='Heart Rate Variability vs Sleep Quality Score')

    fig2.update_traces(mode='lines+markers')
    st.plotly_chart(fig2)
