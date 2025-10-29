import argparse
from extract import extract_data
from transform import transform
from load import get_engine, load_data


def main():
    parser = argparse.ArgumentParser(description="ETL Pipeline CLI")
    parser.add_argument(
        "stage",
        choices=["extract", "transform", "load", "all"],
        help="Этап, который нужно выполнить: extract / transform / load / all",
    )
    args = parser.parse_args()

    FILE_ID = "1lIOnHOtzCNSoXV8akytUimq2RfNTC7PU"

    if args.stage == "extract":
        extract_data(FILE_ID)

    elif args.stage == "transform":
        import pandas as pd
        df_raw = pd.read_csv("data/raw/raw_dataset.csv")
        transform(df_raw)

    elif args.stage == "load":
        engine = get_engine()
        load_data(engine)

    elif args.stage == "all":
        df_raw = extract_data(FILE_ID)
        df_clean = transform(df_raw)
        engine = get_engine()
        load_data(engine)

    else:
        print("Неизвестный аргумент. Используйте extract / transform / load / all.")


if __name__ == "__main__":
    main()
