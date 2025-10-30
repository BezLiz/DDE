import pandas as pd
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Получаем учетные данные
load_dotenv()

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_url = os.getenv("DB_URL")
db_port = os.getenv("DB_PORT")

# Загружаем данные
data = pd.read_parquet("Data_clean.parquet").head(100)
data.info()
# Меняем регистр на нижний и пробелы на _
new_column_names = {col: col.lower().replace(' ', '_') for col in data.columns}
data.rename(columns=new_column_names, inplace=True)
data.info()

# Подключаемся к БД
db_name = 'homeworks'
engine = create_engine(
    f"postgresql+psycopg2://{db_user}:{db_password}@{db_url}:{db_port}/{db_name}", 
    pool_recycle=3600,
)
print("Подключились к базе")

# Загружаем данные
data.to_sql(
    name="bezzubova",
    con=engine,
    schema="public", 
    if_exists="replace", 
    index=False,
)
print("Данные успешно загружены в базу")

# Проверка количества строк в выгруженных данных
with engine.begin() as conn:
    count = conn.execute(text("SELECT COUNT(*) FROM public.bezzubova")).scalar()
    print(f"Количество строк в таблице bezzubova: {count}")

