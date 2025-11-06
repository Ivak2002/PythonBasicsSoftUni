integer_list = input().split()
remove_times = int(input())
integers_as_strings = []
for number in integer_list:
    integers_as_strings.append(int(number))
for min_number in range(remove_times):
    smallest_number = min(integers_as_strings)
    integers_as_strings.remove(smallest_number)
list_without_brackets = str(integers_as_strings)[1:-1]
print(list_without_brackets)
