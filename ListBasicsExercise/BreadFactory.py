events = input().split("|")

energy = 100
coins = 100

for event in events:
    name, number = event.split("-")
    number = int(number)

    if name == "rest":
        gained = min(100 - energy, number)
        energy += gained
        print(f"You gained {gained} energy.")
        print(f"Current energy: {energy}.")

    elif name == "order":
        if energy >= 30:
            energy -= 30
            coins += number
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:  # buying ingredient
        if coins >= number:
            coins -= number
            print(f"You bought {name}.")
        else:
            print(f"Closed! Cannot afford {name}.")
            exit()

print("Day completed!")
print(f"Coins: {coins}")
print(f"Energy: {energy}")
