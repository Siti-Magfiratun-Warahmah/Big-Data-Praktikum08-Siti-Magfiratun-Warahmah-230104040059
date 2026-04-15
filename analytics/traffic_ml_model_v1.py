import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load data clean
df = pd.read_csv('data/clean/traffic_smartcity_clean_v1.csv')

# Feature engineering
df['datetime'] = pd.to_datetime(df['datetime'])
df['hour'] = df['datetime'].dt.hour
df['day'] = df['datetime'].dt.dayofweek

# Lag feature
df['lag1'] = df['traffic'].shift(1)

# Hapus NA
df = df.dropna()

# Tentukan fitur & target
X = df[['hour', 'day', 'lag1']]
y = df['traffic']

# Training model
model = RandomForestRegressor()
model.fit(X, y)

# Simpan model
joblib.dump(model, 'models/traffic_model_v1.pkl')

print("Model berhasil disimpan")