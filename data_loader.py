import pandas as pd

FILE_ID = "1Lg5PhTbw9ZZZzkVjl1kQ0aA9rQjsVQt7"
file_url = f"https://drive.google.com/uc?export=download&id=1Lg5PhTbw9ZZZzkVjl1kQ0aA9rQjsVQt7"
# Чтение данных из CSV файла
try:
    print("Чтение данных из CSV файла...")
    raw_data = pd.read_csv(file_url)

# Проверка результата
    print(raw_data.shape)
    print("Первые 10 строк:")
    print(raw_data.head(10))

except Exception as e:
    print("Ошибка при чтении файла:", e)

# ПРИВЕДЕНИЕ ТИПОВ ДАННЫХ

df = pd.DataFrame(raw_data)

# Разделяем значения pubmed_id, так как они неправильно приведены в датаете
df["Pubmed_ID"] = df["Pubmed_ID"].astype(str).str.split("##")
df = df.explode("Pubmed_ID", ignore_index=True)

print("\nТипы ДО приведения:")
print(df.dtypes)

# Числовые данные
numeric_cols = ["Sequence_Length", "Pubmed_ID"]
for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")
# Категориальные данные
categorical_cols = ["Structure", "Linear/Cyclic/Branched", "Stereochemistry"]
for col in categorical_cols:
    if col in df.columns:
        df[col] = df[col].astype("category")
# Текстовые данные
text_cols = [col for col in df.columns if col not in numeric_cols + categorical_cols]
for col in text_cols:
    df[col] = df[col].astype(str)

print("\nТипы ПОСЛЕ приведения:")
print(df.dtypes)

print("\nПропуски после приведения:")
print(df.isnull().sum())

# Сохранение данных 
out_path = "Data_clean.parquet"
df.to_parquet(out_path, index=False)
print(f"\n[OK] Данные успешно приведены к нужным типам и сохранены в {out_path}")


