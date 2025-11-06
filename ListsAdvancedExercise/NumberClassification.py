def positive_and_negative_numbers(number_sequence):
    positive_numbers_list = []
    negative_numbers_list = []
    for number in number_sequence:
        if number >= 0:
            positive_numbers_list.append(number)
        else:
            negative_numbers_list.append(number)
    return print(f"Positive: {', '.join(str(number) for number in positive_numbers_list)}"), \
           print(f"Negative: {', '.join(str(number) for number in negative_numbers_list)}")


def even_and_odd_numbers(number_sequence):
    even_numbers_list = []
    odd_numbers_list = []
    for number in number_sequence:
        if number % 2 == 0:
            even_numbers_list.append(number)
        else:
            odd_numbers_list.append(number)
    return print(f"Even: {', '.join(str(number) for number in even_numbers_list)}"), \
           print(f"Odd: {', '.join(str(number) for number in odd_numbers_list)}")


numbers = list(map(int, input().split(',')))
number_classified = positive_and_negative_numbers(numbers), even_and_odd_numbers(numbers)
