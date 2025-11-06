def even_result(string_of_numbers):
    result = 0
    for number in string_of_numbers:
        current_number = int(number)
        if current_number % 2 == 0:
            result += current_number
    return result


def odd_result(string_of_numbers):
    result = 0
    for number in string_of_numbers:
        current_number = int(number)
        if current_number % 2 != 0:
            result += current_number
    return result


string_of_digits = input()
result_of_even_summary = even_result(string_of_digits)
result_of_odd_summary = odd_result(string_of_digits)
print(f"Odd sum = {result_of_odd_summary}, Even sum = {result_of_even_summary}")