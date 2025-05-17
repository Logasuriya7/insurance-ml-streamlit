import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open('insurance_model.pkl', 'rb'))

# Title
st.title("Insurance Cost Prediction App")

# Input fields
age = st.slider("Age", 18, 100, 30)
sex = st.selectbox("Sex", ['Male', 'Female'])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0, step=1)
smoker = st.selectbox("Smoker", ['Yes', 'No'])
region = st.selectbox("Region", ['northeast', 'northwest', 'southeast', 'southwest'])

# Encoding categorical variables
sex_encoded = 1 if sex == 'Male' else 0
smoker_encoded = 1 if smoker == 'Yes' else 0
region_mapping = {'northeast': 0, 'northwest': 1, 'southeast': 2, 'southwest': 3}
region_encoded = region_mapping[region]

# Prediction
if st.button("Predict Insurance Cost"):
    input_data = np.array([[age, sex_encoded, bmi, children, smoker_encoded, region_encoded]])
    prediction = model.predict(input_data)
    st.success(f"Estimated Insurance Cost: ${prediction[0]:,.2f}")