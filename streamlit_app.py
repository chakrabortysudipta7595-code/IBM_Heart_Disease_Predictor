import streamlit as st
import pickle
import numpy as np
import os

MODEL_PATH = 'models/heart_disease_model.pkl'
SCALER_PATH = 'models/scaler.pkl'
FEATURES_PATH = 'models/feature_names.pkl'


@st.cache_resource
def load_artifacts():
    model = None
    scaler = None
    feature_names = None
    try:
        if os.path.exists(MODEL_PATH):
            model = pickle.load(open(MODEL_PATH, 'rb'))
        if os.path.exists(SCALER_PATH):
            scaler = pickle.load(open(SCALER_PATH, 'rb'))
        if os.path.exists(FEATURES_PATH):
            feature_names = pickle.load(open(FEATURES_PATH, 'rb'))
    except Exception as e:
        st.error(f'Error loading model artifacts: {e}')
    return model, scaler, feature_names


def main():
    st.set_page_config(page_title='Heart Disease Predictor', layout='centered')
    st.title('Heart Disease Prediction')
    st.markdown('Upload or use the form below to predict the presence of heart disease.')

    model, scaler, feature_names = load_artifacts()

    if model is None or scaler is None:
        st.warning('Model or scaler not found. Please run `python train_model.py` to generate model artifacts.')
        return

    with st.form('prediction_form'):
        age = st.slider('Age', 20, 100, 50)
        sex = st.selectbox('Sex', options={0: 'Female', 1: 'Male'}.items(), format_func=lambda x: x[1])
        sex = list({0: 'Female', 1: 'Male'}.keys())[list({0: 'Female', 1: 'Male'}.values()).index(sex[1])]
        cp = st.selectbox('Chest Pain Type (cp)', options=[0, 1, 2, 3])
        trestbps = st.number_input('Resting Blood Pressure (trestbps)', min_value=80, max_value=250, value=120)
        chol = st.number_input('Serum Cholesterol (chol)', min_value=100, max_value=700, value=200)
        fbs = st.selectbox('Fasting blood sugar > 120 mg/dl (fbs)', options=[0, 1])
        restecg = st.selectbox('Resting electrocardiographic results (restecg)', options=[0, 1, 2])
        thalach = st.number_input('Maximum heart rate achieved (thalach)', min_value=60, max_value=250, value=150)
        exang = st.selectbox('Exercise induced angina (exang)', options=[0, 1])
        oldpeak = st.number_input('ST depression (oldpeak)', min_value=0.0, max_value=10.0, value=1.0, format="%f")
        slope = st.selectbox('Slope of ST segment (slope)', options=[0, 1, 2])
        ca = st.selectbox('Number of major vessels colored by fluoroscopy (ca)', options=[0, 1, 2, 3, 4])
        thal = st.selectbox('Thalassemia (thal)', options=[0, 1, 2, 3])

        submit = st.form_submit_button('Predict')

    if submit:
        try:
            features = np.array([
                float(age),
                float(sex),
                float(cp),
                float(trestbps),
                float(chol),
                float(fbs),
                float(restecg),
                float(thalach),
                float(exang),
                float(oldpeak),
                float(slope),
                float(ca),
                float(thal)
            ]).reshape(1, -1)

            features_scaled = scaler.transform(features)
            pred = model.predict(features_scaled)[0]
            proba = model.predict_proba(features_scaled)[0]

            st.write('### Prediction')
            if pred == 1:
                st.error('Heart Disease Detected')
            else:
                st.success('No Heart Disease Detected')

            st.write('**Probability**')
            st.write(f'No disease: {proba[0]*100:.2f}%')
            st.write(f'Disease: {proba[1]*100:.2f}%')

        except Exception as e:
            st.exception(e)


if __name__ == '__main__':
    main()
