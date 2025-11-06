positive_numbers_list = []
negative_numbers_list = []
number_of_integers = int(input())
counter_of_positive_numbers = 0
sum_of_negative_numbers = 0
for number in range(number_of_integers):
    current_digit = int(input())
    if current_digit >= 0:
        positive_numbers_list.append(current_digit)
        counter_of_positive_numbers += 1
    else:
        negative_numbers_list.append(current_digit)
        sum_of_negative_numbers += current_digit
print(f"{positive_numbers_list}\n"
      f"{negative_numbers_list}\n"
      f"Count of positives: {counter_of_positive_numbers}\n"
      f"Sum of negatives: {sum_of_negative_numbers}")
