rewards_list = list(int(number) for number in input().split(", "))
number_of_beggars = int(input())
given_rewards_list = list()
first_beggar = 0
for beggar in range(number_of_beggars):
    beggar_sum = 0
    for current_beggar in range(first_beggar, len(rewards_list), number_of_beggars):
        beggar_sum += rewards_list[current_beggar]
    given_rewards_list.append(beggar_sum)
    first_beggar += 1
print(given_rewards_list)