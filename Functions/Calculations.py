def calculator(first_number,second_number,operator):
    if operator == "multiply":
        result = first_number * second_number
    elif operator == "divide":
        result = first_number // second_number
    elif operator == "add":
        result = first_number + second_number
    else:
        result = first_number - second_number

    print(result)


math_sing = input()
number_one = int(input())
number_two = int(input())
calculator(number_one,number_two,math_sing)