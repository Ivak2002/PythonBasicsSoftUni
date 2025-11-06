def round_value_list(numbers):
    numbers_list_round_value = []
    for digit in numbers:
        current_digit =float(digit)
        abs_digit = round(current_digit)
        numbers_list_round_value.append(abs_digit)
    return numbers_list_round_value


user_input = input().split()
user_input = round_value_list(user_input)
print(user_input)
