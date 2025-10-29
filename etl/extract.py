import pandas as pd
import os
from pathlib import Path


def extract_data(file_id: str, output_dir: str = 'data/raw') -> pd.DataFrame:
    """
    Загружает сырые данные из Google Drive по file_id и сохраняет в CSV.
    """
    file_url = f"https://drive.google.com/uc?export=download&id={file_id}"
    os.makedirs(output_dir, exist_ok=True)
    save_path = Path(output_dir) / "raw_dataset.csv"

    try:
        print("Чтение данных из CSV файла...")
        df = pd.read_csv(file_url, na_values=["#NUM!"])
    except Exception as e:
        raise RuntimeError(f"Ошибка при чтении файла: {e}")

    if df.empty:
        raise ValueError("CSV-файл пуст.")

    print(f"Размер данных: {df.shape}")
    print("Первые 10 строк:")
    print(df.head(10))

    print("\nКоличество пропусков по столбцам:")
    print(df.isnull().sum())

    duplicates = df.duplicated().sum() 
    print(f"\nКоличество дубликатов: {duplicates}")

    try:
        df.to_csv(save_path, index=False, encoding="utf-8")
        print(f"\nИсходные данные успешно сохранены в {save_path}")
    except Exception as e:
        raise RuntimeError(f"Ошибка при сохранении CSV: {e}")

    return df


if __name__ == "__main__":
    FILE_ID = "1lIOnHOtzCNSoXV8akytUimq2RfNTC7PU"
    extract_data(FILE_ID)
