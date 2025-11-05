number_of_pourings = int(input())
tank_capacity = 255
pourings = 0
for pouring in range(number_of_pourings):
    current_pouring = int(input())
    if tank_capacity >= current_pouring:
        tank_capacity -= current_pouring
        pourings += current_pouring
    else:
        print("Insufficient capacity!")
print(pourings)
