def next_version(version):
    """
    This function updates the software to its next version.
    """
    version[-1] += 1
    for number in range(len(version)-1, 0, -1):
        if version[number] > 9:
            version[number] = 0
            version[number-1] += 1

    return version


current_version = [int(digit) for digit in input().split('.')]
updated_version = next_version(current_version)
print(".".join(str(digit) for digit in updated_version))
