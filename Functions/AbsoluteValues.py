def absolute_value_list(numbers:list):
    numbers_list_abs_value = []
    for digit in numbers:
        current_digit = float(digit)
        abs_digit = abs(current_digit)
        numbers_list_abs_value.append(abs_digit)
    return numbers_list_abs_value


user_input = input().split()
user_input = absolute_value_list(user_input)
print(user_input)