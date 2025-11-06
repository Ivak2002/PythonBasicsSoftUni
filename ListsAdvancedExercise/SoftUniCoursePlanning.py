def add(schedule, lesson):
    if lesson not in schedule:
        schedule.append(lesson)
    return schedule


def insert(schedule, lesson, index):
    if lesson not in schedule:
        schedule.insert(index, lesson)
    return schedule


def remove_lesson(schedule, lesson):
    if lesson in schedule:
        schedule.remove(lesson)
    if f"{lesson}-Exercise" in schedule:
        schedule.remove(f"{lesson}-Exercise")
    return schedule


def swap(schedule, l1, l2):
    if l1 in schedule and l2 in schedule:
        i1, i2 = schedule.index(l1), schedule.index(l2)
        schedule[i1], schedule[i2] = schedule[i2], schedule[i1]

        # move exercises
        for lesson in (l1, l2):
            ex = f"{lesson}-Exercise"
            if ex in schedule:
                schedule.remove(ex)
                schedule.insert(schedule.index(lesson) + 1, ex)

    return schedule


def exercise(schedule, lesson):
    ex = f"{lesson}-Exercise"

    if lesson in schedule:
        if ex not in schedule:
            schedule.insert(schedule.index(lesson) + 1, ex)
    else:
        schedule.append(lesson)
        schedule.append(ex)

    return schedule


schedule = input().split(", ")

command = input()
while command != "course start":
    parts = command.split(":")
    action = parts[0]

    if action == "Add":
        schedule = add(schedule, parts[1])

    elif action == "Insert":
        schedule = insert(schedule, parts[1], int(parts[2]))

    elif action == "Remove":
        schedule = remove_lesson(schedule, parts[1])

    elif action == "Swap":
        schedule = swap(schedule, parts[1], parts[2])

    elif action == "Exercise":
        schedule = exercise(schedule, parts[1])

    command = input()

for i, lesson in enumerate(schedule, 1):
    print(f"{i}.{lesson}")
