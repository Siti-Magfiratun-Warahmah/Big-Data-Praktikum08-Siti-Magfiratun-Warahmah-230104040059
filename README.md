# PRAKTIKUM 7 – Machine Learning untuk Prediksi Traffic (Smart City AI)

**Proyek:** BIGDATA-SPARK-230104040059

Program ini dibuat untuk memenuhi instruksi **Praktikum 7 Mata Kuliah Teknologi Big Data**. Praktikum ini berfokus pada penerapan **Machine Learning untuk prediksi traffic** menggunakan data time series serta pembangunan dashboard interaktif berbasis Streamlit.

Pipeline yang dibangun merupakan pengembangan dari praktikum sebelumnya, dengan fokus pada integrasi data, pemodelan Machine Learning, serta visualisasi hasil prediksi dalam konteks Smart City.

---

# 👩‍🎓 Identitas Mahasiswa

| Keterangan     | Informasi                              |
| -------------- | -------------------------------------- |
| Mata Kuliah    | Teknologi Big Data                     |
| Dosen Pengampu | Muhayat, S.Ag., M.IT                   |
| Praktikum      | Praktikum 7 – Machine Learning Traffic |
| Nama Mahasiswa | Siti Magfiratun Warahmah               |
| NIM            | 230104040059                           |
| Kelas          | TI23B                                  |

---

# 🚀 Deskripsi Program

Program ini merupakan implementasi sistem **Machine Learning untuk prediksi traffic** dalam konteks Smart City. Sistem ini memanfaatkan data historis berbasis waktu (time series) untuk memprediksi jumlah kendaraan pada waktu tertentu.

Proses dimulai dari data mentah yang kemudian dibersihkan, dilanjutkan dengan pembuatan fitur (feature engineering), pelatihan model Machine Learning menggunakan algoritma Random Forest, hingga penyajian hasil dalam bentuk dashboard interaktif.

Sistem ini tidak hanya menampilkan data, tetapi juga mampu memberikan prediksi yang dapat digunakan sebagai dasar pengambilan keputusan dalam pengelolaan lalu lintas.

---

# 🏗️ Arsitektur Pipeline

Pipeline Machine Learning pada praktikum ini menggunakan alur berikut:

```
Data Raw
   │
   ▼
Data Clean
   │
   ▼
Feature Engineering
   │
   ▼
Model Training (Random Forest)
   │
   ▼
Dashboard (Streamlit)
   │
   ▼
Insight & Prediction
```

Penjelasan alur data:

1. **Data Raw** berupa dataset traffic yang berisi informasi waktu dan jumlah kendaraan.
2. **Data Cleaning** dilakukan untuk mengubah format datetime, mengurutkan data, dan menghapus nilai kosong.
3. **Feature Engineering** menambahkan fitur penting seperti jam, hari, dan traffic sebelumnya (lag).
4. **Model Training** menggunakan Random Forest Regressor untuk mempelajari pola data.
5. **Dashboard** menampilkan visualisasi dan hasil prediksi secara interaktif.
6. **Insight & Prediction** digunakan untuk memahami pola traffic dan melakukan estimasi kondisi di masa depan.

---

# 🛠️ Teknologi yang Digunakan

* Python 3
* Pandas
* Scikit-learn (Random Forest)
* Joblib
* Matplotlib
* Streamlit
* Visual Studio Code
* WSL (Linux)
* Bash CLI

---

# 📊 Dataset

Dataset yang digunakan adalah:

```
traffic_smartcity_v1.csv
```

Dataset ini berisi data traffic berbasis waktu yang digunakan untuk proses analisis dan prediksi.

---

# ⚙️ Cara Kerja Program

## 1️⃣ Data Cleaning

Melakukan pembersihan data dengan:

* Mengubah kolom datetime ke format waktu
* Mengurutkan data berdasarkan waktu
* Menghapus data kosong

Output disimpan pada folder `data/clean`.

---

## 2️⃣ Feature Engineering & Modeling

Menambahkan fitur:

* Hour (jam)
* Day (hari)
* Lag1 (traffic sebelumnya)

Kemudian model dilatih menggunakan Random Forest dan disimpan dalam bentuk file `.pkl`.

---

## 3️⃣ Dashboard & Prediksi

Dashboard dibangun menggunakan Streamlit dan menampilkan:

### Visualisasi

* Grafik traffic (trend)
* Statistik rata-rata dan maksimum traffic

### Prediksi

* Input: jam, hari, traffic sebelumnya
* Output: jumlah kendaraan (prediksi)

---

# 📂 Struktur Folder Project

```
bigdata-project
│
├── data/
│   ├── raw/
│   └── clean/
│
├── scripts/
├── analytics/
├── models/
├── dashboard/
│
└── README.md
```

---

# ▶️ Cara Menjalankan Program

Aktifkan virtual environment:

```
source venv/bin/activate
```

Install dependency:

```
pip install pandas scikit-learn matplotlib streamlit joblib
```

Jalankan program:

### 1. Data Cleaning

```
python scripts/traffic_data_cleaning_v1.py
```

### 2. Modeling

```
python analytics/traffic_ml_model_v1.py
```

### 3. Dashboard

```
streamlit run dashboard/traffic_dashboard_v1.py
```

---

# 🌐 Akses Dashboard

Buka di browser:

```
http://localhost:8501
```

---

# 🎯 Kesimpulan

Praktikum ini berhasil mengimplementasikan sistem Machine Learning untuk prediksi traffic dengan memanfaatkan data historis dan fitur sederhana seperti jam, hari, dan traffic sebelumnya. Pipeline yang dibangun berjalan secara terstruktur mulai dari data cleaning hingga visualisasi dashboard, serta mampu menghasilkan prediksi yang dapat digunakan untuk memahami pola lalu lintas dan mendukung pengambilan keputusan dalam Smart City.

---

# 📦 Repository

```
https://github.com/Siti-Magfiratun-Warahmah/Big-Data-Praktikum07-Siti-Magfiratun-Warahmah-230104040059
```
