def modify_values(lst, removed):
    for i in range(len(lst)):
        if lst[i] <= removed:
            lst[i] += removed
        else:
            lst[i] -= removed
    return lst


def pokemon_go(sequence):
    removed_sum = 0

    while sequence:
        idx = int(input())

        if idx < 0:
            removed = sequence[0]
            removed_sum += removed
            sequence[0] = sequence[-1]
        elif idx >= len(sequence):
            removed = sequence[-1]
            removed_sum += removed
            sequence[-1] = sequence[0]
        else:
            removed = sequence.pop(idx)
            removed_sum += removed

        sequence = modify_values(sequence, removed)

    return removed_sum


numbers = list(map(int, input().split()))
print(pokemon_go(numbers))
