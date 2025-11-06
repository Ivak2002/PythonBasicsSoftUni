happiness_list = list(map(int, input().split()))
happiness_factor = int(input())
happiness_list_multiplied = list(map(lambda grade: grade * happiness_factor, happiness_list))
average_happiness = list(filter(lambda grade: grade >= (sum(happiness_list_multiplied) / len(happiness_list_multiplied))
                                , happiness_list_multiplied))

if len(average_happiness) >= len(happiness_list) / 2:
    print(f"Score: {len(average_happiness)}/{len(happiness_list)}. Employees are happy!")
else:
    print(f"Score: {len(average_happiness)}/{len(happiness_list)}. Employees are not happy!")
