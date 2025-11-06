fires = input().split("#")
water = int(input())

cells_put_out = []
effort = 0
total_fire = 0

for cell in fires:
    fire_type, value = cell.split(" = ")
    value = int(value)

    valid = False
    if fire_type == "High" and 81 <= value <= 125:
        valid = True
    elif fire_type == "Medium" and 51 <= value <= 80:
        valid = True
    elif fire_type == "Low" and 1 <= value <= 50:
        valid = True

    if valid and water >= value:
        water -= value
        cells_put_out.append(value)
        effort += value * 0.25
        total_fire += value

print("Cells:")
for c in cells_put_out:
    print(f"- {c}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
