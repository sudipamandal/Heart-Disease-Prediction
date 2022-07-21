import pickle
import streamlit as st
import numpy as np

model = pickle.load(open("model.pkl","rb"))

def main():
    st.title("Heart Disease Prediction")
    st.subheader("Predict if a person has a heart disease or not")
    
    data = []
    age = st.number_input("Enter the age : ")
    data.append(age)
    sex = st.number_input("Enter the sex (Male : 1, Female : 0): ",0, 1)
    data.append(sex)
    chest_pain_type = st.number_input("Enter the chest pain type : ",0, 3)
    data.append(chest_pain_type)
    resting_bp = st.number_input("Enter the resting blood pressure : ")
    data.append(resting_bp)    
    serum_cholestoral = st.number_input("Enter the serum cholestoral in mg/dl : ")
    data.append(serum_cholestoral)
    fasting_blood_sugar = st.number_input("Enter the fasting blood sugar : ")
    data.append(fasting_blood_sugar)
    resting_ecg_results = st.number_input("Enter the resting electrocardiographic results : ", 0, 2)
    data.append(resting_ecg_results)
    max_heart_rate = st.number_input("Enter the maximum heart rate achieved : ")
    data.append(max_heart_rate)
    exercise_induced_angina = st.number_input("Enter the exercise induced angina : ")
    data.append(exercise_induced_angina)
    oldpeak = st.number_input("Enter the oldpeak (ST depression induced by exercise relative to rest) : ")
    data.append(oldpeak)
    slope = st.number_input("Enter the slope of the peak exercise ST segment : ")
    data.append(slope)
    number_of_major_vessels = st.number_input("Enter the number of major vessels (0-3) colored by flourosopy : ", 0, 3)
    data.append(number_of_major_vessels)
    thal = st.number_input("Enter thal value (0 = normal; 1 = fixed defect; 2 = reversable defect) : ", 0, 2)
    data.append(thal)
    
    if st.button("Predict"):
        data_as_numpy_array= np.asarray(data)
        data_reshaped = data_as_numpy_array.reshape(1,-1)
        prediction = model.predict(data_reshaped)
        result = prediction[0]
        
        if result == 1:
            st.error("The Person has a Heart Disease")
        else:
            st.success("The Person does not have a Heart Disease")

main()
    