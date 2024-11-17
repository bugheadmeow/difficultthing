# TODO решите задачу
import json
INPUT_FILE = "input.json"
def task() -> float:
    total = 0.0
    with open(INPUT_FILE) as input_file:
        json_data = json.load(input_file)

        for item in json_data:
            score = item["score"]
            weight = item["weight"]
            total += item["score"] * item["weight"]
    return round(total, 3)
print(task())
