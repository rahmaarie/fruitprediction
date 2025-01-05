import streamlit as st
import joblib
import numpy as np

# Memuat model, scaler, dan label_encoder
classifier = joblib.load('svm_model.pkl')
scaler = joblib.load('scaler.pkl')
label_encoder = joblib.load('label_encoder.pkl')

# Judul aplikasi
st.title("Fruit Classifier App")
st.write("Prediksi spesies buah berdasarkan fitur-fitur seperti diameter, berat, dan nilai RGB warna.")

# Input pengguna
st.sidebar.header("Masukkan fitur buah:")
diameter = st.sidebar.slider("Diameter:", min_value=0.0, max_value=50.0,step=0.1)
weight = st.sidebar.slider("Weight:", min_value=0.0, max_value=1000.0, step=1.0)
red = st.sidebar.slider("Red :", 0, 255)
green = st.sidebar.slider("Green :", 0, 255)
blue = st.sidebar.slider("Blue :", 0, 255)

# Tombol prediksi
if st.sidebar.button("Prediksi"):
    # Data input
    input_features = np.array([[diameter, weight, red, green, blue]])
    
    # Scaling data
    input_scaled = scaler.transform(input_features)
    
    # Prediksi dengan model
    prediction = classifier.predict(input_scaled)
    
    # Menampilkan hasil
    predicted_species = label_encoder.inverse_transform(prediction)
    st.subheader("Hasil Prediksi:")
    st.write(f"Spesies buah yang diprediksi: **{predicted_species[0]}**")
    
    # Menampilkan gambar berdasarkan prediksi
    if predicted_species[0] == "orange":
        st.image("images/orange.jpg", caption="Orange", width=300)
    elif predicted_species[0] == "grapefruit":
        st.image("images/grapefruit.jpg", caption="Grapefruit", width=300)

