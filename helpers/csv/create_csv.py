import csv


def create_csv_for_2gis(goods: list):
    with open("classmates.csv", mode="w", encoding='utf-8') as csv_file:
        names = ["name", "price", "category", "url", "picture", "description"]
        file_writer = csv.DictWriter(csv_file, delimiter=",", lineterminator="\r", fieldnames=names)
        file_writer.writeheader()
        for good in goods:
            file_writer.writerow(good)
        # file_writer.writerow({"Имя": "Вова", "Возраст": "14"})


if __name__ == '__main__':
    create_csv_for_2gis([
        {"name": "Футболка", "price": "1", "category": "2", "url": "3", "description": "4", "picture": "5"},
    ])
