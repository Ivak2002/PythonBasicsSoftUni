def smallest_number(number_one,number_two,number_three):
    numbers_list = [number_one,number_two,number_three]
    biggest_number = min(numbers_list)
    return biggest_number


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(smallest_number(first_number,second_number,third_number))