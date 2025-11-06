def min_number(numbers):
    return min(numbers)


def max_number(numbers):
    return max(numbers)


def summary_of_numbers(numbers):
    return sum(numbers)


list_of_numbers = list(map(int,input().split()))
lowest_number = min_number(list_of_numbers)
maximum_number = max_number(list_of_numbers)
summary_of_all_numbers = summary_of_numbers(list_of_numbers)

print(f"The minimum number is {lowest_number}\n"
      f"The maximum number is {maximum_number}\n"
      f"The sum number is: {summary_of_all_numbers}")
