while True:
    name_student = input()
    name_student_length = len(name_student)

    if name_student == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    if name_student == "Voldemort":
        print("You must not speak of that name!")
        break

    if name_student_length < 5:
        print(f"{name_student} goes to Gryffindor.")
    elif name_student_length == 5:
        print(f"{name_student} goes to Slytherin.")
    elif name_student_length == 6:
        print(f"{name_student} goes to Ravenclaw.")
    else:
        print(f"{name_student} goes to Hufflepuff.")





