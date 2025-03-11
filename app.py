import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title = "Prediction of Diseases Outbreaks",
                   layout ='wide',
                   page_icon="🩺")


working_dir = os.path.dirname(os.path.abspath(__file__))

diabetes_model = pickle.load(open(r"/workspaces/Prediction-of-Diseases-Outbreak/saved_model/Diabetes_model.sav",'rb'))
heart_model = pickle.load(open(r"/workspaces/Prediction-of-Diseases-Outbreak/saved_model/heart_disease_model.sav",'rb'))
parkinson_model = pickle.load(open(r"/workspaces/Prediction-of-Diseases-Outbreak/saved_model/parkinson_model.sav",'rb'))

with st.sidebar:
    selected = option_menu('Prediction of Diseases Outbreaks System ',
                            
                            ['Diabetes Prediction',
                             'Heart Diseases Prediction',  # Fixed capitalization
                             'Parkinson Prediction'],
                            menu_icon = 'hospital-fill',
                            icons = ['activity', 'heart','person'],
                            default_index=0)
                            
if selected == 'Diabetes Prediction':

    st.title('Diabetes prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        pregnancies = st.text_input('Number of Pregnancies')
    
    with col2:
        Glucose = st.text_input("Glucose Level")
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    
    with col1:
        skinThickness = st.text_input('Skin Thickness Value')
    
    with col2:
        Insulin = st.text_input('Insulin level')

    with col3:
        BMI = st.text_input('BMI Value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')

    with col2:
        Age= st.text_input('Age of the Person')

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        
        user_input = [pregnancies, Glucose, BloodPressure, skinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = "The person is diabetic"
        else:
            diab_diagnosis = "The Person is not diabetic"
    
    st.success(diab_diagnosis)

if selected == 'Heart Diseases Prediction':  # Fixed to match sidebar menu

    st.title('Heart diseases prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    
    with col2:
        sex = st.text_input("Sex")
    
    with col3:
        cp = st.text_input('Chest Pain Type')
    
    with col1:
        restbps = st.text_input('Resting Blood Pressure')
    
    with col2:
        chol = st.text_input('Serum Cholestrol in mg/dl')

    with col3:
        fbs = st.text_input('Fatsing Blood Sugar')
    
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')

    with col3:
        exang = st.text_input('Excercise Induced Angina')

    with col1:
        oldpeak = st.text_input('St depression induced by excercise')

    with col2:
        slope = st.text_input('Slope of the peak excerise ST segment')
    
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal:0 = normal; 1= fixed defect; 2=reversable defect')

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        
        user_input = [age,sex,cp,restbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = "The person is having heart diseases"
        else:
            heart_diagnosis = "The Person does not have a heart diseases"
    
    st.success(heart_diagnosis)

if selected == 'Parkinson Prediction':  # Fixed to match sidebar menu

    st.title('Parkinson diseases prediction using ML')

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    
    with col2:
        fhi = st.text_input("MDVP:Fhi(Hz)")
    
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')
    
    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimer_db = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
    
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')
    
    with col4:
        DDA = st.text_input('Shimmer:DDA')
    
    with col5:
        NHR = st.text_input('NHR')
    
    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')
    
    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')
    
    parkinson_diagnosis = ''

    if st.button('Parkinson Disease Test Result'):
        
        user_input = [fo,fhi,flo,Jitter_percent,Jitter_Abs,RAP,PPQ,
                      DDP,Shimer,Shimer_db,APQ3,APQ5,APQ,DDA,
                      NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]

        user_input = [float(x) for x in user_input]

        parkinson_prediction = parkinson_model.predict([user_input])

        if parkinson_prediction[0] == 1:
            parkinson_diagnosis = "The person is having parkinson diseases"
        else:
            parkinson_diagnosis = "The Person does not have a parkinson diseases"
    
    st.success(parkinson_diagnosis)