# Fruit Classifier App

## Background Problem
Dalam dunia pertanian dan industri pangan, identifikasi buah berdasarkan karakteristik fisik dan warna merupakan tantangan yang sering dihadapi. Banyak sistem masih mengandalkan identifikasi manual yang rentan terhadap kesalahan manusia. Oleh karena itu, diperlukan solusi otomatis yang dapat memprediksi spesies buah dengan akurasi tinggi berdasarkan fitur seperti diameter, berat, dan nilai RGB warna.

**Tujuan proyek ini:**
- Mengembangkan model machine learning untuk mengklasifikasikan spesies buah berdasarkan fitur yang diberikan.
- Membangun aplikasi berbasis web menggunakan Streamlit untuk memudahkan pengguna dalam melakukan prediksi.
- Menyediakan tampilan visual berupa gambar buah yang sesuai dengan hasil prediksi.

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

## Library yang Digunakan
- **Pemrograman**: Python
- **Framework Web**: Streamlit
- **Machine Learning**: Scikit-learn
- **Pengolahan Data**: NumPy, Pandas

## Insight
Dari hasil implementasi dan pengujian model, berikut beberapa insight yang diperoleh:
1. Fitur warna (RGB) memiliki peran yang signifikan dalam membedakan spesies buah.
2. Model SVM mampu mengklasifikasikan buah dengan tingkat akurasi yang cukup baik.
3. Dengan tambahan lebih banyak data latih, model ini berpotensi memiliki akurasi yang lebih tinggi.

## Advice
Project ini dapat dikembangkan lebih lanjut ke beberapa aspek berikut:
1. Menggunakan model deep learning seperti CNN untuk meningkatkan akurasi klasifikasi.
2. Menambahkan fitur deteksi dari gambar langsung menggunakan OpenCV.
3. Mengembangkan aplikasi mobile berbasis Android/iOS agar lebih mudah digunakan oleh pengguna.


