# PRAKTIKUM 8 – Real-Time Fraud Detection (Kafka + Spark + Streamlit)

**Proyek:** BIGDATA-SPARK-230104040059

Program ini dibuat untuk memenuhi instruksi **Praktikum 8 Mata Kuliah Teknologi Big Data**. Praktikum ini berfokus pada pembangunan sistem **Real-Time Fraud Detection** menggunakan Apache Kafka, Apache Spark Structured Streaming, serta visualisasi dashboard dengan Streamlit.

Pipeline yang dibangun merupakan pengembangan dari praktikum sebelumnya, dengan fokus pada **real-time processing, keamanan data, serta integrasi sistem end-to-end** dalam konteks industri perbankan modern.

---

# 👩‍🎓 Identitas Mahasiswa

| Keterangan     | Informasi                               |
| -------------- | --------------------------------------- |
| Mata Kuliah    | Teknologi Big Data                      |
| Dosen Pengampu | Muhayat, S.Ag., M.IT                    |
| Praktikum      | Praktikum 8 – Real-Time Fraud Detection |
| Nama Mahasiswa | Siti Magfiratun Warahmah                |
| NIM            | 230104040059                            |
| Kelas          | TI23B                                   |

---

# 🚀 Deskripsi Program

Program ini merupakan implementasi sistem **deteksi fraud transaksi bank secara real-time** menggunakan arsitektur Big Data modern.

Sistem bekerja dengan cara:

* Mengirim data transaksi secara streaming menggunakan Kafka
* Memproses data secara real-time menggunakan Spark Structured Streaming
* Menerapkan data masking dan enkripsi untuk keamanan
* Mengklasifikasikan transaksi sebagai FRAUD atau NORMAL
* Menampilkan hasil dalam dashboard interaktif

Sistem ini mencerminkan implementasi nyata pada industri perbankan yang membutuhkan **kecepatan, keamanan, dan skalabilitas tinggi**.

---

# 🏗️ Arsitektur Pipeline

```
Kafka (Producer)
   ↓
Spark Streaming (Processing)
   ↓
Secure Processing (Masking + Encryption + Fraud Detection)
   ↓
Storage (Parquet)
   ↓
Dashboard (Streamlit)
```

Penjelasan alur:

1. Kafka Producer mengirim data transaksi secara real-time.
2. Spark Streaming membaca data dari Kafka.
3. Data diproses dengan:

   * Masking data rekening
   * Enkripsi jumlah transaksi
   * Deteksi fraud berbasis rule
4. Data disimpan dalam format Parquet.
5. Dashboard menampilkan hasil secara real-time.

---

# 🔐 Konsep Keamanan yang Digunakan

* **Data Masking** → Menyembunyikan nomor rekening
* **Encryption (Base64)** → Mengamankan nilai transaksi
* **Logging** → Monitoring aktivitas sistem

**Fraud Detection Rule-Based:**

* Jumlah > 50.000.000 → FRAUD
* Lokasi luar negeri → FRAUD

---

# 🛠️ Teknologi yang Digunakan

* Python 3
* Apache Kafka
* Apache Spark (PySpark)
* Pandas
* Streamlit
* Java (OpenJDK 11)
* WSL (Linux)
* Bash CLI
* VS Code

---

# 📂 Struktur Folder Project

```
bigdata-project
│
├── scripts/
│   ├── kafka_producer_bank.py
│   ├── spark_streaming_fraud_v2.py
│
├── dashboard/
│   └── fraud_dashboard_v2.py
│
├── stream_data/
│   └── realtime_output/
│
├── data/
│   └── checkpoints/
│
├── logs/
│   └── fraud_realtime.log
│
└── README.md
```

---

# ⚙️ Cara Menjalankan Program

## 1️⃣ Aktifkan Virtual Environment

```
source venv/bin/activate
```

---

## 2️⃣ Jalankan Kafka

**Terminal 1 (Zookeeper)**

```
cd kafka_2.13-3.5.1
bin/zookeeper-server-start.sh config/zookeeper.properties
```

**Terminal 2 (Kafka Server)**

```
cd kafka_2.13-3.5.1
bin/kafka-server-start.sh config/server.properties
```

**Terminal 3 (Create Topic)**

```
bin/kafka-topics.sh --create \
--topic bank_topic \
--bootstrap-server localhost:9092 \
--partitions 1 \
--replication-factor 1
```

---

## 3️⃣ Jalankan Sistem

**Terminal 1 (Producer)**

```
python3 scripts/kafka_producer_bank.py
```

**Terminal 2 (Spark Streaming)**

```
spark-submit \
--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 \
scripts/spark_streaming_fraud_v2.py
```

**Terminal 3 (Dashboard)**

```
streamlit run dashboard/fraud_dashboard_v2.py
```

---

# 🌐 Akses Dashboard

Buka di browser:

```
http://localhost:8501
```

---

# 📊 Output Sistem

Sistem menghasilkan:

* Data transaksi real-time
* Status fraud (FRAUD / NORMAL)
* File output dalam format Parquet

Dashboard visualisasi:

* Total transaksi
* Total fraud
* Tabel data
* Grafik distribusi

---

# 📸 Output Wajib

* Script Python
* Folder `stream_data/realtime_output`

Screenshot:

* Kafka berjalan
* Spark berjalan
* Dashboard tampil

---

# 🎯 Kesimpulan

Praktikum ini berhasil mengimplementasikan sistem **Real-Time Fraud Detection berbasis Big Data** dengan memanfaatkan Kafka, Spark, dan Streamlit.

Pipeline yang dibangun mampu:

* Mengolah data secara real-time
* Mengamankan data sensitif melalui masking dan enkripsi
* Mendeteksi fraud secara cepat
* Menampilkan hasil secara interaktif

Sistem ini menunjukkan bahwa dalam Big Data, **kecepatan dan keamanan merupakan dua aspek utama yang tidak dapat dipisahkan**.

---

# 📦 Repository

```
https://github.com/Siti-Magfiratun-Warahmah/Big-Data-Praktikum08-Siti-Magfiratun-Warahmah-230104040059
```
