import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from pathlib import Path


def get_engine():
    """
    Создание подключения к базе данных PostgreSQL.
    """
    load_dotenv()
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    url = os.getenv("DB_URL")
    port = os.getenv("DB_PORT")
    dbname = "homeworks"

    if not all([user, password, url, port, dbname]):
        raise ValueError("Не все переменные окружения заданы!")

    engine_url = f"postgresql+psycopg2://{user}:{password}@{url}:{port}/{dbname}"
    engine = create_engine(engine_url, pool_recycle=3600)
    print("Подключение к базе данных установлено.")
    return engine


def load_data(engine, parquet_path: str = "data/processed/clean_dataset.parquet", table_name: str = "bezzubova"):
    """
    Загрузка первых 100 строк очищенных данных в PostgreSQL.
    """
    df = pd.read_parquet(parquet_path).head(100)

    print(f"\nРазмер выгружаемого набора данных: {df.shape}")

    # Приведение названий столбцов к нижнему регистру и замена пробелов
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]

    df.to_sql(
        name=table_name,
        con=engine,
        schema="public",
        if_exists="replace",
        index=False,
    )
    print(f"Данные успешно загружены в таблицу public.{table_name}")

    with engine.begin() as conn:
        count = conn.execute(text(f"SELECT COUNT(*) FROM public.{table_name}")).scalar()
        print(f"Количество строк в таблице {table_name}: {count}")


if __name__ == "__main__":
    engine = get_engine()
    load_data(engine)
