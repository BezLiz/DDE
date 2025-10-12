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




