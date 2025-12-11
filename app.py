import streamlit as st
import pickle
import numpy as np

with open("Assets/model.pkl", "rb") as file:
    model = pickle.load(file)

with open("Assets/label_encoder.pkl", "rb") as file:
    encoder = pickle.load(file)

st.set_page_config(page_title="Shoe Size Prediction", page_icon="👟", layout="centered")

st.markdown(
    """
    <style>
    body {
        background-color: #f9f9f9;
    }
    .main {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
    }
    h1 {
        color: #2196F3; /* Light Blue */
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    .stButton button {
        background-color: #2196F3;
        color: white;
        border-radius: 8px;
        height: 3em;
        width: 100%;
        font-size: 16px;
        font-weight: bold;
    }
    .stButton button:hover {
        background-color: #1976D2; /* Darker Blue on Hover */
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='color:#2196F3; text-align:center;'>👟 Shoe Size Prediction App</h1>", unsafe_allow_html=True)
st.write("Enter your details below and get your *predicted shoe size* instantly!")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input(" Age", min_value=10, max_value=70, value=25)

with col2:
    height = st.number_input(" Height (cm)", min_value=100, max_value=220, value=170)

gender = st.selectbox("Gender", encoder.classes_)

gender_encoded = encoder.transform([gender])[0]

features = np.array([[age, height, gender_encoded]])

if st.button("Predict Shoe Size"):
    prediction = model.predict(features)

    st.markdown(
        f"""
        <div style="
            background-color: #add8e6; 
            padding: 16px; 
            border-radius: 10px; 
            text-align: center; 
            font-size: 20px; 
            font-weight: bold;
            color: #000000;
            margin-top: 12px;
        ">
            👟 Predicted Shoe Size: {prediction[0]:.2f}
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Developed by HABIB UR REHMAN </p>", unsafe_allow_html=True)
