number_of_strings = int(input())

for string in range(number_of_strings):
    current_string = input()

    if current_string.__contains__(",") or current_string.__contains__(".") or current_string.__contains__("_"):
        print(f"{current_string} is not pure!")
    else:
        print(f"{current_string} is pure.")

