# TODO решите задачу
import json


def task() -> float:
    filename = 'input.json'
    with open(filename, 'r') as file:
        data = json.load(file)
    sum = 0
    for item in data:
        asum=1
        for items in item.values():
            asum = items * asum
        sum += asum

    return round(sum, 3)



print(task())
