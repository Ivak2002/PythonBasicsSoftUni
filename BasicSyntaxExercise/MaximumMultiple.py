divisor_number = int(input())
divide_number = int(input())

for number in range(divide_number,divisor_number, -1):
    current_number = int(number)

    if current_number % divisor_number == 0:
        print(current_number)
        break
