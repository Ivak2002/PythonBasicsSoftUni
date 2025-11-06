def electron_placing(number):
    electrons_list = []
    for electrons in range(1,number + 1):
        max_electrons = 2 * electrons ** 2
        if number >= max_electrons:
            electrons_list.append(max_electrons)
            number -= max_electrons
            if number == 0:
                break
        else:
            electrons_list.append(number)
            break
    return electrons_list


electrons_numbers = int(input())
distributed_electrons = electron_placing(electrons_numbers)
print(distributed_electrons)
