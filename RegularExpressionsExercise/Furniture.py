import re

pattern = r">>([A-Za-z]+)<<(\d+(\.\d+)?)!(\d+)"
items = []
total = 0

while True:
    line = input()
    if line == "Purchase":
        break

    match = re.search(pattern, line)
    if match:
        name = match.group(1)
        price = float(match.group(2))
        qty = int(match.group(4))
        items.append(name)
        total += price * qty

print("Bought furniture:")
for item in items:
    print(item)
print(f"Total money spend: {total:.2f}")
