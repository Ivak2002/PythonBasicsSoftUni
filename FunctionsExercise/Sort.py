def sort_in_ascending_order(numbers_sequence):
    sorted_list = sorted(numbers_sequence)
    return sorted_list


sequence_of_integers = map(int,input().split())
sorted_sequence_of_integers = sort_in_ascending_order(sequence_of_integers)
print(sorted_sequence_of_integers)
