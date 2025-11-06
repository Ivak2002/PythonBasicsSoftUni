factor_number = int(input())
count_number = int(input())
result_list = []
for number in range(1,count_number + 1):
    result = factor_number * number
    result_list.append(result)
print(result_list)
