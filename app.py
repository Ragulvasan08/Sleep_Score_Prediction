import streamlit as st
import pandas as pd
import plotly.graph_objects as go

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

# Data Visualization using Plotly Graph Objects
with st.expander('Data Visualization'):
    st.write('**Line Chart with Enhanced Presentation**')

    # Create a plotly figure
    fig = go.Figure()

    # Add trace for Sleep Duration vs Sleep Quality Score
    fig.add_trace(go.Scatter(
        x=ds.index, 
        y=ds['Sleep_Duration_Hours'],
        mode='lines+markers',
        name='Sleep Duration (Hours)',
        line=dict(color='royalblue', width=2),
        marker=dict(color='royalblue', size=6)
    ))

    # Add trace for Sleep Quality Score
    fig.add_trace(go.Scatter(
        x=ds.index, 
        y=ds['Sleep_Quality_Score'],
        mode='lines+markers',
        name='Sleep Quality Score',
        line=dict(color='firebrick', width=2),
        marker=dict(color='firebrick', size=6)
    ))

    # Customize layout for better appearance
    fig.update_layout(
        title='Sleep Duration vs Sleep Quality Score',
        xaxis_title='Index',
        yaxis_title='Value',
        font=dict(family="Arial", size=12),
        legend=dict(
            title="Metrics",
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showline=True, showgrid=False),
        yaxis=dict(showline=True, showgrid=False)
    )

    # Show the chart in Streamlit
    st.plotly_chart(fig)
    
    # You can add more charts for different metrics similarly
    # For example: Heart Rate Variability vs Sleep Quality Score
    fig2 = go.Figure()

    # Add trace for Heart Rate Variability
    fig2.add_trace(go.Scatter(
        x=ds.index, 
        y=ds['Heart_Rate_Variability'],
        mode='lines+markers',
        name='Heart Rate Variability',
        line=dict(color='green', width=2),
        marker=dict(color='green', size=6)
    ))

    # Add trace for Sleep Quality Score
    fig2.add_trace(go.Scatter(
        x=ds.index, 
        y=ds['Sleep_Quality_Score'],
        mode='lines+markers',
        name='Sleep Quality Score',
        line=dict(color='firebrick', width=2),
        marker=dict(color='firebrick', size=6)
    ))

    # Customize layout for the second chart
    fig2.update_layout(
        title='Heart Rate Variability vs Sleep Quality Score',
        xaxis_title='Index',
        yaxis_title='Value',
        font=dict(family="Arial", size=12),
        legend=dict(
            title="Metrics",
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showline=True, showgrid=False),
        yaxis=dict(showline=True, showgrid=False)
    )

    st.plotly_chart(fig2)
