# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as input_file:
        reader = csv.DictReader(input_file)
        for row in reader:
            print(row)

    with open (OUTPUT_FILENAME) as output_file:
        json.dumps(output_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME, encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")