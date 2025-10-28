import pandas as pd
from pathlib import Path

FILE_ID = "1lIOnHOtzCNSoXV8akytUimq2RfNTC7PU"
file_url = f"https://drive.google.com/uc?export=download&id={FILE_ID}"
out_path = Path("Data_clean.parquet")

try:
    print("Чтение данных из CSV файла...")
    raw_data = pd.read_csv(file_url, na_values=["#NUM!"])

# Проверка результата
    print(raw_data.shape)
    print("Первые 10 строк:")
    print(raw_data.head(10))

except Exception as e:
    print("Ошибка при чтении файла:", e)

# ПРИВЕДЕНИЕ ТИПОВ ДАННЫХ

df = pd.DataFrame(raw_data)

print("\nТипы ДО приведения:")
print(df.dtypes)

# Текстовые данные
text_cols = ["row ID", "Molecule", "Molecule name", "Molecular Formula"]
for col in text_cols:
    df[col] = df[col].astype(str)

# Числовые данные
numeric_cols = [col for col in df.columns if col not in text_cols]
for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce").astype("float64")

print("\nТипы ПОСЛЕ приведения:")
print(df.dtypes)

print("\nПропуски после приведения:")
print(df.isnull().sum())

# Сохранение данных
try:
    df.to_parquet(out_path, index=False, engine="pyarrow")
    print(f"\n[OK] Данные успешно приведены к нужным типам и сохранены в {out_path}")
except Exception as e:
    print("Ошибка при сохранении файла:", e)