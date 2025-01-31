
import streamlit as st
import pandas as pd
# import zipfile
import joblib
# import pickle
# import os
# import gdown


# URL of the file on Google Drive
# file_url = 'https://drive.google.com/file/d/1qHveJ_xH3lrz3H5J1vzYV5rFQxzTVbNb'

# Download the file
# gdown.download(file_url, 'y_pred_prob_knn.pkl', quiet=False)

# Load the model
model = joblib.load('y_pred_lr.pkl')


# Load the model (make sure you have a model file named 'accident_model.pkl')
# model = joblib.load('y_pred_prob_knn.pkl')
# with open('y_pred_prob_knn.pkl', 'rb') as f:
#     dataset = pickle.load(f)

# Streamlit app
st.title('Accident Severity Prediction')

# Collect user input
Time = st.text_input('Time')
Day_of_week = st.selectbox('Day of Week', ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
Age_band_of_driver = st.selectbox('Age band of driver', ['0-18', '19-30', '31-50', '51-65', '65+'])
Sex_of_driver = st.selectbox('Sex of driver', ['Male', 'Female'])
Educational_level = st.selectbox('Educational level', ['None', 'Primary', 'Secondary', 'Higher'])
Vehicle_driver_relation = st.selectbox('Vehicle driver relation', ['Owner', 'Non-owner'])
Driving_experience = st.selectbox('Driving experience (years)', ['<1', '1-2', '2-5', '5-10', '10+'])
Type_of_vehicle = st.selectbox('Type of vehicle', ['Car', 'Truck', 'Motorcycle', 'Bicycle', 'Other'])
Owner_of_vehicle = st.selectbox('Owner of vehicle', ['Owner', 'Non-owner'])
Service_year_of_vehicle = st.number_input('Service year of vehicle', min_value=0, max_value=50, step=1)
Type_of_collision = st.selectbox('Type of collision', ['Head-on', 'Rear-end', 'Side', 'Rollover', 'Other'])
Vehicle_movement = st.selectbox('Vehicle movement', ['Moving', 'Parked', 'Stopped'])
Casualty_class = st.selectbox('Casualty class', ['Driver', 'Passenger', 'Pedestrian'])
Sex_of_casualty = st.selectbox('Sex of casualty', ['Male', 'Female'])
Age_band_of_casualty = st.selectbox('Age band of casualty', ['0-18', '19-30', '31-50', '51-65', '65+'])
Casualty_severity = st.selectbox('Casualty severity', ['Minor', 'Serious', 'Fatal'])
Work_of_casuality = st.selectbox('Work of casualty', ['Employed', 'Student', 'Unemployed', 'Retired'])
Pedestrian_movement = st.selectbox('Pedestrian movement', ['Walking', 'Running', 'Standing', 'Other'])
Cause_of_accident = st.text_input('Cause of accident')
Accident_severity = st.selectbox('Accident severity', ['Low', 'Medium', 'High'])

# Create dataframe 
input_data = pd.DataFrame({
    'Time': [Time],
    'Day_of_week': [Day_of_week],
    'Age_band_of_driver': [Age_band_of_driver],
    'Sex_of_driver': [Sex_of_driver],
    'Educational_level': [Educational_level],
    'Vehicle_driver_relation': [Vehicle_driver_relation],
    'Driving_experience': [Driving_experience],
    'Type_of_vehicle': [Type_of_vehicle],
    'Owner_of_vehicle': [Owner_of_vehicle],
    'Service_year_of_vehicle': [Service_year_of_vehicle],
    'Type_of_collision': [Type_of_collision],
    'Vehicle_movement': [Vehicle_movement],
    'Casualty_class': [Casualty_class],
    'Sex_of_casualty': [Sex_of_casualty],
    'Age_band_of_casualty': [Age_band_of_casualty],
    'Casualty_severity': [Casualty_severity],
    'Work_of_casuality': [Work_of_casuality],
    'Pedestrian_movement': [Pedestrian_movement],
    'Cause_of_accident': [Cause_of_accident],
    'Accident_severity': [Accident_severity]
})

# Predict button
if st.button('Predict'):
    # Make a prediction
    prediction = model.predict(input_data)
    
    # Display the prediction
    st.write(f'Prediction: {prediction[0]}')
