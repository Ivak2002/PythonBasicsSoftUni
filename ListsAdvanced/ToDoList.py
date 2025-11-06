notes_list = [0] * 10
while True:
    note = input()
    if note == "End":
        while 0 in notes_list:
            notes_list.remove(0)
        print(notes_list)
        break

    task = note.split("-")
    priority = int(task[0]) - 1
    to_do = task[1]
    notes_list.pop(priority)
    notes_list.insert(priority,to_do)











