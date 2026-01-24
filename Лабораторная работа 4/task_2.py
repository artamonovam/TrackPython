# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла
    clov = []
    with (open(INPUT_FILENAME, 'r') as file):
        reader = csv.DictReader(file)
        for row in reader:
            clov.append(row)

    with open(OUTPUT_FILENAME, 'w') as file:
        json.dump(clov, file, indent=4)
    ...  # TODO Сериализовать в файл с отступами равными 4




if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
