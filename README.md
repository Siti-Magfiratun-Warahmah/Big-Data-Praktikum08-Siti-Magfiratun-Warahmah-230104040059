# PRAKTIKUM 5 – Big Data Analytics & Decision-Oriented System

**Proyek:** BIGDATA-SPARK-230104040059

Program ini dibuat untuk memenuhi instruksi **Praktikum 5 Mata Kuliah Teknologi Big Data**. Praktikum ini berfokus pada implementasi **Big Data Analytics berbasis streaming** serta pembangunan **Decision-Oriented System** menggunakan **Apache Spark Structured Streaming** dan **Streamlit**.

Pipeline yang dibangun mensimulasikan sistem **Smart Transportation Analytics**, dimana data perjalanan diproses secara real-time untuk menghasilkan insight dan alert yang mendukung pengambilan keputusan.

---

# 👩‍🎓 Identitas Mahasiswa

| Keterangan     | Informasi                                   |
| -------------- | ------------------------------------------- |
| Mata Kuliah    | Teknologi Big Data                          |
| Dosen Pengampu | Muhayat, S.Ag., M.IT                        |
| Praktikum      | Praktikum 5 – Big Data Analytics & Use Case |
| Nama Mahasiswa | Siti Magfiratun Warahmah                    |
| NIM            | 230104040059                                |
| Kelas          | TI23B                                       |

---

# 🚀 Deskripsi Program

Program ini merupakan implementasi **streaming data pipeline berbasis Smart Transportation** yang digunakan untuk memproses data perjalanan secara real-time.

Pada praktikum ini dilakukan simulasi **event streaming** menggunakan trip generator yang menghasilkan data perjalanan secara berkala. Data tersebut kemudian diproses menggunakan **Spark Structured Streaming**, disimpan dalam **Parquet Data Lake**, dan dianalisis untuk menghasilkan insight serta alert secara otomatis.

Pipeline ini tidak hanya menampilkan data, tetapi juga membangun **Decision-Oriented System** yang mampu memberikan informasi penting secara real-time.

---

# 🏗️ Arsitektur Pipeline

Pipeline Big Data Analytics pada praktikum ini menggunakan arsitektur berikut:

```
Trip Generator (JSON)
        │
        ▼
stream_data/transportation
        │
        ▼
Spark Structured Streaming
        │
        ▼
Parquet Data Lake
data/serving/transportation
        │
        ▼
Analytics Layer (Python)
        │
        ▼
Alert System
        │
        ▼
Real-Time Dashboard (Streamlit)
```

Penjelasan alur data:

1. **Trip Generator** menghasilkan data perjalanan (trip) secara berkala dalam format JSON.
2. Data disimpan pada folder **stream_data/transportation**.
3. **Spark Structured Streaming** membaca data sebagai streaming.
4. Data diproses dan disimpan dalam format **Parquet** pada data lake.
5. **Analytics Layer** menghasilkan metrik dan insight.
6. **Alert System** mendeteksi kondisi tertentu.
7. **Dashboard** menampilkan visualisasi real-time.

---

# 🛠️ Teknologi yang Digunakan

* Python 3.12
* Apache Spark (PySpark)
* Spark Structured Streaming
* Parquet Data Lake
* Streamlit
* Pandas
* Visual Studio Code
* WSL Ubuntu
* Bash CLI

Teknologi ini digunakan untuk membangun sistem **real-time analytics dan decision system** berbasis Big Data.

---

# 📊 Dataset Streaming

Dataset tidak berasal dari file statis, tetapi dihasilkan secara dinamis oleh **trip generator**.

Contoh struktur data:

```
{
  "trip_id": "TRX123",
  "vehicle_type": "Car",
  "location": "Jakarta",
  "distance": 12.5,
  "fare": 45000,
  "timestamp": "2026-03-31 17:45:20"
}
```

Data disimpan pada folder:

```
stream_data/transportation
```

---

# ⚙️ Cara Kerja Program

## 1️⃣ Trip Generator

Script `trip_generator.py` menghasilkan data perjalanan secara berkala.

Data berisi:

* trip_id
* vehicle_type
* location
* distance
* fare
* timestamp

---

## 2️⃣ Streaming Processing

Script `streaming_trip_layer.py` membaca data streaming menggunakan Spark Structured Streaming.

Data diproses dengan konsep:

```
readStream()
writeStream()
trigger(processingTime="5 seconds")
```

Hasil disimpan dalam format Parquet pada:

```
data/serving/transportation
```

---

## 3️⃣ Analytics & Alert System

Data yang telah diproses kemudian dianalisis untuk menghasilkan:

* Total trips
* Total fare
* Top location
* Peak hour
* Mobility trend
* Vehicle distribution

Sistem juga menghasilkan alert seperti:

* High traffic volume
* High fare detected

---

## 4️⃣ Real-Time Dashboard

Dashboard dibangun menggunakan **Streamlit**.

Menampilkan:

### Key Metrics

* Total Trips
* Total Fare
* Top Location
* Peak Hour

### Visualisasi

* Fare per Location
* Vehicle Distribution
* Mobility Trend

### Data

* Live Trip Data
* Abnormal Trips

Dashboard diperbarui secara otomatis secara real-time.

---

# 📂 Struktur Folder Project

```
BIGDATA-PROJECT
│
├── scripts/
│   └── transportation/
│
├── analytics/
│
├── alerts/
│
├── dashboard/
│
├── data/
│   └── serving/
│       └── transportation/
│
└── README.md
```

---

# ▶️ Cara Menjalankan Program

Install dependency:

```
pip install pyspark streamlit pandas pyarrow
```

Jalankan pipeline menggunakan 3 terminal:

### Terminal 1 — Spark Streaming

```
spark-submit scripts/transportation/streaming_trip_layer.py
```

### Terminal 2 — Trip Generator

```
python scripts/transportation/trip_generator.py
```

### Terminal 3 — Dashboard

```
streamlit run dashboard/dashboard_transportation.py
```

---

# 🌐 Akses Dashboard

Buka di browser:

```
http://localhost:8501
```

---

# 🎯 Kesimpulan

Praktikum ini mengimplementasikan sistem **Big Data Analytics berbasis streaming** yang mampu memproses data perjalanan secara real-time menggunakan Spark Structured Streaming.

Data yang dihasilkan oleh trip generator diproses, disimpan dalam Parquet Data Lake, dan dianalisis untuk menghasilkan insight serta alert. Dashboard Streamlit menampilkan informasi tersebut secara real-time sehingga sistem tidak hanya berfungsi sebagai visualisasi, tetapi juga sebagai **Decision-Oriented System** yang mendukung pengambilan keputusan berbasis data.

---

# 📦 Repository

```
https://github.com/Siti-Magfiratun-Warahmah/Big-Data-Praktikum05-Siti-Magfiratun-Warahmah-230104040059
```
