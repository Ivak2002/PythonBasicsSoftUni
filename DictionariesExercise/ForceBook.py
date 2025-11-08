sides = {}

def find_user(user):
    for side, users in sides.items():
        if user in users:
            return side
    return None

while True:
    line = input()
    if line == "Lumpawaroo":
        break

    if " | " in line:
        side, user = line.split(" | ")
        if not find_user(user):
            sides.setdefault(side, []).append(user)

    else:  # user -> side
        user, side = line.split(" -> ")
        old_side = find_user(user)
        if old_side:
            sides[old_side].remove(user)
        sides.setdefault(side, []).append(user)
        print(f"{user} joins the {side} side!")

for side, users in sides.items():
    if users:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")
