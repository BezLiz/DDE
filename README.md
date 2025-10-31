# DDE
[*Ссылка на датасет (Google Drive)*](https://drive.google.com/file/d/1lIOnHOtzCNSoXV8akytUimq2RfNTC7PU/view?usp=sharing)

## Описание проекта
Проект по анализу и обработке данных по химическим дескрипторам.

### Основные задачи:
- прочтение, анализ и сохранение исходного датасета
- трансформация и сохранение преобразованого датасета
- проведение разведочного анализа данных (EDA) с визуализацией
- запись данных в базу данных PostgreSQL 

## Структура проекта
```
DDE/
├── etl/                      # ETL пакет
│ ├── extract.py              # Извлечение, оценка и сохранение сырых данных в .cvs
│ ├── transform.py            # Проверка и приведение типов данных, сохранение очищенных данных в .parquet
│ ├── load.py                 # Выгрузка 100 строк данных из .parquet в базу данных PostgreSQL 
│ └── main.py                 # Cбор скриптов вместе и предоставление CLI-интерфейса
│
├── experiments/ 
│ ├── data_loader.py          # Скрипт чтения датасета с Google Drive
│ └── write_to_db.py          # Скрипт записи данных в базу PostgreSQL 
│
├── notebooks/                
│   └── EDA.ipynb             # Разведочный анализ данных 
│
├── .gitignore                # Игнорируемые файлы и папки
├── README.md                 # Основная документация проекта
├── poetry.lock               # Фиксированные версии зависимостей Poetry
├── pyproject.toml            # Конфигурация зависимостей Poetry
└── raw_data.png              # Пример вывода первых срок сырого датасета
```

## **Начало работы**

Создание окружение conda
```bash
conda create -n my_env python pip
```
Активация окружения 
```bash
conda activate my_env
```
Установка poetry
```bash
pip install poetry
```
Создание файла зависимостей в папке пректа
```bash
poetry init
```
Добавление нужных библиотек
```bash
poetry add jupiterlab pandas matplotlib wget
```
Установка зависимостей 
```bash
poetry install --no-root
```
Запуск скрипта для чтения датасета 
```bash
python data_loader.py
```
## **Вывод первых 10 строк**
![Первые 10 строк:](raw_data.png)

## **Exploratory Data Analysis (EDA)** 
Анализ датасета химических дескрипторов

[*Ссылка на рендер ноутбуков*](https://nbviewer.org/github/BezLiz/DDE/blob/main/notebooks/EDA.ipynb)

Цели анализа:
- изучить структуру данных
- проверить их полноту и целостность 
- оценить выбросы
- выявить взаимосвязи

## **ETL**
Структура
```
etl/
├── extract.py  # Извлечение, оценка и сохранение сырых данных в .cvs
├── transform.py  # Проверка и приведение типов данных, сохранение очищенных данных в .parquet
├── load.py  # Выгрузка 100 строк данных из .parquet в базу данных PostgreSQL homeworks
└── main.py  # Cбор скриптов вместе и предоставление CLI-интерфейса
```

Запуск полного процесса etl
``` bash
python etl/main.py all
```
Запуск файлов по отдельности
``` bash
python etl/main.py extract
python etl/main.py transform
python etl/main.py load
```
