import pandas as pd
import os
from pathlib import Path


def transform(df: pd.DataFrame, output_dir: str = 'data/processed') -> pd.DataFrame:
    """
    Приведение типов данных и сохранение очищенного датасета в .parquet.
    """
    os.makedirs(output_dir, exist_ok=True)
    out_path = Path(output_dir) / "clean_dataset.parquet"

    print("\nТипы данных ДО приведения:")
    print(df.dtypes)

    # Текстовые и числовые колонки
    text_cols = ["row ID", "Molecule", "Molecule name", "Molecular Formula"]
    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].astype(str)

    numeric_cols = [col for col in df.columns if col not in text_cols]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").astype("float64")

    print("\nТипы данных ПОСЛЕ приведения:")
    print(df.dtypes)

    try:
        df.to_parquet(out_path, index=False, engine="pyarrow")
        print(f"\nОчищенные данные сохранены в {out_path}")
    except Exception as e:
        raise RuntimeError(f"Ошибка при сохранении parquet: {e}")

    return df


if __name__ == "__main__":
    raw_path = Path("data/raw/raw_dataset.csv")
    df_raw = pd.read_csv(raw_path)
    transform(df_raw)
