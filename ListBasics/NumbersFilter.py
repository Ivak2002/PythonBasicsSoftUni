number_of_digits = int(input())
list_of_all_digits = []
filtered_list = []
for number in range(number_of_digits):
    current_number = int(input())
    list_of_all_digits.append(current_number)

command = input()
if command == "even":
    for digit in list_of_all_digits:
        if digit % 2 == 0 or digit == 0:
            filtered_list.append(digit)
elif command == "odd":
    for digit in list_of_all_digits:
        if digit % 2 != 0:
            filtered_list.append(digit)
elif command == "negative":
    for digit in list_of_all_digits:
        if digit < 0:
            filtered_list.append(digit)
else:
    for digit in list_of_all_digits:
        if digit > 0 or digit == 0:
            filtered_list.append(digit)

print(filtered_list)