final_number = int(input())


for number in range(1, final_number + 1):
    current_number = number
    current_number_string = str(number)
    digit_sum = 0

    for digit in current_number_string:
        current_digit = int(digit)
        digit_sum += current_digit

    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        print(f"{number} -> True")
    else:
        print(f"{number} -> False")
