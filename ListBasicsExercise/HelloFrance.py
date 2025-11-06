items = input().split("|")
budget = float(input())

bought = []
profit = 0

for item in items:
    item_type, price = item.split("->")
    price = float(price)

    valid = False
    if item_type == "Clothes" and price <= 50:
        valid = True
    elif item_type == "Shoes" and price <= 35:
        valid = True
    elif item_type == "Accessories" and price <= 20.50:
        valid = True

    if valid and budget >= price:
        budget -= price
        new_price = price * 1.40
        bought.append(new_price)
        profit += new_price - price

print(" ".join(f"{price:.2f}" for price in bought))
print(f"Profit: {profit:.2f}")

final_budget = budget + sum(bought)

if final_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
