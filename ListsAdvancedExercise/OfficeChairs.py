number_of_rooms = int(input())
left_chairs = 0

is_enough = True
for room in range(1,number_of_rooms + 1):
    current_room = input().split()
    visitors_in_current_room = int(current_room[-1])
    chairs_in_current_room = current_room[-2]
    result = len(chairs_in_current_room) - visitors_in_current_room
    if result < 0:
        print(f"{abs(result)} more chairs needed in room {room}")
        is_enough = False
    left_chairs += result


if is_enough:
    print(f"Game On, {left_chairs} free chairs left")







