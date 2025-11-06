def even_numbers(numbers_sequence):
    filtered_numbers = []
    for number in numbers_sequence:
        current_number = int(number)
        if current_number % 2 == 0:
            filtered_numbers.append(current_number)
    return filtered_numbers


digits_sequence = input().split()
filtered_digits = even_numbers(digits_sequence)
print(filtered_digits)