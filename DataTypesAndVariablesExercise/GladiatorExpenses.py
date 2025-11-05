lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

shield_breaks = 0
total_expenses = 0.0

for fight in range(1, lost_fights + 1):

    helmet_broken = (fight % 2 == 0)
    sword_broken = (fight % 3 == 0)

    if helmet_broken:
        total_expenses += helmet_price

    if sword_broken:
        total_expenses += sword_price

    # Shield breaks when BOTH helmet and sword break
    if helmet_broken and sword_broken:
        shield_breaks += 1
        total_expenses += shield_price

        # Every 2nd shield break → armor breaks
        if shield_breaks % 2 == 0:
            total_expenses += armor_price

print(f"Gladiator expenses: {total_expenses:.2f} aureus")
