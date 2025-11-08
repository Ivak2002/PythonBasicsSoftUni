n = int(input())
parking = {}

for _ in range(n):
    parts = input().split()

    if parts[0] == "register":
        user, plate = parts[1], parts[2]
        if user in parking:
            print(f"ERROR: already registered with plate number {parking[user]}")
        else:
            parking[user] = plate
            print(f"{user} registered {plate} successfully")

    else:  # unregister
        user = parts[1]
        if user not in parking:
            print(f"ERROR: user {user} not found")
        else:
            parking.pop(user)
            print(f"{user} unregistered successfully")

for user, plate in parking.items():
    print(f"{user} => {plate}")
