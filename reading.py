import json

with open("peoples.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Данні з фалйу:\n")

for surname, info in data.items():
    name, patronymic, year = info
    print(f"{surname} {name} {patronymic}, {year} року народження")
