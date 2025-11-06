numbers_list = list(map(int,input().split(', ')))
filtered_list = list(filter(lambda number: numbers_list[number] % 2 == 0, range(len(numbers_list))))
print(filtered_list)