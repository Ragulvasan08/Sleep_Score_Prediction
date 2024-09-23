import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Set page config with icon and layout
st.set_page_config(page_title="Sleep Score Predictor", page_icon="😴", layout="wide")

# Custom CSS for additional styling
st.markdown("""
    <style>
    /* Main background color and font */
    .main {
        background-color: #e3f2fd;
        font-family: 'Arial', sans-serif;
    }
    /* Header styling */
    h1 {
        color: #0073e6;
        font-size: 3rem;
    }
    /* Sidebar header styling */
    .css-1d391kg h2 {
        color: #0073e6;
        font-size: 1.5rem;
    }
    /* Sidebar panel design */
    .css-1d391kg p {
        font-size: 1.1rem;
        color: #333;
        font-weight: bold;
    }
    /* Success box styling */
    .stAlert {
        background-color: #4caf50;
        border-radius: 10px;
        padding: 20px;
        font-size: 1.5rem;
        color: white;
    }
    /* Footer styling */
    .footer {
        text-align: center;
        font-size: 1.2rem;
        color: #0073e6;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and Info section
st.title('😴 Sleep Score Prediction APP')
st.info('This application predicts your sleep quality score based on several factors using machine learning algorithms.')

# Section: Sidebar Input Features
with st.sidebar:
    st.header('Customize Input Features')

    # Input sliders
    Heart_Rate_Variability = st.slider("💓 Heart Rate Variability (ms)", 0.0, 100.0, 50.0, step=0.1, help="The variation in time intervals between heartbeats.")
    Body_Temperature = st.slider("🌡️ Body Temperature (°C)", 0.0, 100.0, 36.5, step=0.1, help="The average temperature of your body.")
    Sleep_Duration_Hours = st.slider("🛏️ Sleep Duration (hrs)", 0.0, 12.0, 8.0, step=0.1, help="Total number of hours you sleep per day.")
    Caffeine_Intake_mg = st.slider("☕ Caffeine Intake (mg)", 0.0, 500.0, 100.0, step=1.0, help="The amount of caffeine you consume daily.")
    Bedtime_Consistency = st.slider("⏲️ Bedtime Consistency (hrs)", 0.0, 10.0, 1.0, step=0.1, help="How consistent your bedtime routine is.")
    Light_Exposure_hours = st.slider("💡 Light Exposure (hrs)", 0.0, 24.0, 5.0, step=0.1, help="The number of hours exposed to light during the day.")

    # Create input DataFrame
    input_data = {'Heart_Rate_Variability': Heart_Rate_Variability,
                  'Body_Temperature': Body_Temperature,
                  'Sleep_Duration_Hours': Sleep_Duration_Hours,
                  'Caffeine_Intake_mg': Caffeine_Intake_mg,
                  'Bedtime_Consistency': Bedtime_Consistency,
                  'Light_Exposure_hours': Light_Exposure_hours}

    input_df = pd.DataFrame([input_data])
    st.write("**Selected Input Data**")
    st.dataframe(input_df)

# Section: Prediction Model
st.subheader("🤖 Sleep Quality Score Prediction")

# Loading the dataset for training
ds = pd.read_csv('https://raw.githubusercontent.com/Ragulvasan08/Sleep_Score_Prediction/refs/heads/main/Sleep_Quality.csv')
ds.drop(columns=['Movement_During_Sleep', 'Stress_Level'], axis=1, inplace=True)
X = ds.drop('Sleep_Quality_Score', axis=1)
Y = ds['Sleep_Quality_Score']

# Train the RandomForestRegressor
regressor = RandomForestRegressor()
regressor.fit(X, Y)

# Predicting the Sleep Quality Score
prediction = regressor.predict(input_df)

# Displaying Prediction
st.success(f"🎉 Your Predicted Sleep Quality Score is: **{prediction[0]:.2f}**")

# Footer section
st.markdown("""
<hr style="border:1px solid #eee"/>
<div class="footer">
    Made with ❤️ by Ragul | Powered by Machine Learning
</div>
""", unsafe_allow_html=True)
