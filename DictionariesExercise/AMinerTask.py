resources = {}

while True:
    item = input()
    if item == "stop":
        break
    quantity = int(input())
    resources[item] = resources.get(item, 0) + quantity

for item, qty in resources.items():
    print(f"{item} -> {qty}")
