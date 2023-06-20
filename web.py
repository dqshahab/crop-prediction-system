import streamlit as st

import pickle

model = pickle.load(open('model.pkl', 'rb'))

st.title('Crop Prediction System')

von = st.text_input('Enter value of Nitrogen (N):')
vop = st.text_input('Enter value of Phosphorus (P):')
vok = st.text_input('Enter value of Potassium (K):')
vot = st.text_input('Enter value of Temperature:')
voh = st.text_input('Enter value of Humidity:')
voph = st.text_input('Enter value of pH:')
vor = st.text_input('Enter value of Rainfall:')

if st.button('Predict'):
    try:
        
        von = float(von)
        vop = float(vop)
        vok = float(vok)
        vot = float(vot)
        voh = float(voh)
        voph = float(voph)
        vor = float(vor)
        data = [[von,vop,vok,vot,voh,voph,vor]]
        result = model.predict(data)
        st.success(result[0])
    except ValueError:
        st.error("Please enter numeric values only.")
        
