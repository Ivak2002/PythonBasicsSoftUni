def add_people(cart,humans):
    cart[-1] += humans
    return cart


def insert_people(cart,place,humans):
    cart[place] += humans
    return cart


def remove_people(cart,place,humans):
    cart[place] -= humans
    return cart


number_of_wagons = int(input())
wagons = list()
for wagon in range(number_of_wagons):
    wagons.append(0)


while True:
    command = input()
    if command == "End":
        print(wagons)
        break
    if "add" in command:
        command = command.split()
        people = int(command[1])
        add_people(wagons,people)
    elif "insert" in command:
        command = command.split()
        index = int(command[1])
        people = int(command[2])
        insert_people(wagons,index,people)
    elif "leave" in command:
        command = command.split()
        index = int(command[1])
        people = int(command[2])
        remove_people(wagons, index, people)







