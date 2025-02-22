# Fruit Classifier App

## Deskripsi
Fruit Classifier App adalah aplikasi berbasis web yang dibuat menggunakan Streamlit untuk memprediksi spesies buah berdasarkan fitur seperti diameter, berat, dan nilai RGB warna.

## Fitur
- **Input data menggunakan slider** untuk memasukkan fitur buah:
  - Diameter
  - Berat
  - Nilai warna RGB (Red, Green, Blue)
- **Prediksi spesies buah** menggunakan model *Supervised Learning* (SVM)
- **Menampilkan gambar buah** yang diprediksi sesuai hasil klasifikasi

## Instalasi
### 1. Clone Repository
```bash
git clone https://github.com/username/fruit-classifier.git
cd fruit-classifier
```

### 2. Install Dependensi
Pastikan Python telah terinstal, kemudian jalankan perintah berikut:
```bash
pip install -r requirements.txt
```

### 3. Jalankan Aplikasi
```bash
streamlit run appfruit.py
```

## Contoh Penggunaan
1. Jalankan aplikasi dengan `streamlit run appfruit.py`.
2. Masukkan fitur buah menggunakan slider.
3. Klik tombol **"Prediksi"**.
4. Aplikasi akan menampilkan spesies buah yang diprediksi beserta gambarnya.

## Library yang digunakan
- Python
- Streamlit
- Scikit-learn
- NumPy
- Pandas


