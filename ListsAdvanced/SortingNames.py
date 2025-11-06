def sort_names(names_string):
    names = names_string.split(", ")

    # Sort by: length DESC, then name ASC
    sorted_names = sorted(names, key=lambda n: (-len(n), n))

    return sorted_names


names_input = input()
print(sort_names(names_input))
