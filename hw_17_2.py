"""
это строка существует толькл ради pylint и не для чего больше
"""
import json
import requests

if __name__ == "__main__":
    response = requests.get("https://jsonplaceholder.typicode.com/todos/", timeout=10)
    data = response.json()
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f)

    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    for i, item in enumerate(data, start=1):
        with open(f"item_{i}.json", "w", encoding="utf-8") as f:
            json.dump(item, f)
