while True:
    string = input()
    repetition = 2

    if string == "End":
        break

    if string == "SoftUni":
        continue
    else:
        new_string = ''.join([char*repetition for char in string])
        print(new_string)

