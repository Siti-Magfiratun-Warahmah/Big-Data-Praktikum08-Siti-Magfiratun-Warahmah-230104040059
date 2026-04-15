import pandas as pd

# Load data
df = pd.read_csv('data/raw/traffic_smartcity_v1.csv')

# Ubah ke datetime
df['datetime'] = pd.to_datetime(df['datetime'])

# Urutkan data
df = df.sort_values('datetime')

# Hapus data kosong
df = df.dropna()

# Simpan hasil clean
df.to_csv('data/clean/traffic_smartcity_clean_v1.csv', index=False)

print("Data cleaning selesai")