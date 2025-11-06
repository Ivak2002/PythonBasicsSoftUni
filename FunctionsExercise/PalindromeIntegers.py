def palindrome_checker(numbers):
    """
    This function checks if a number is  palindromic.
    A palindrome is a number that is read the same backward and forward (323,1001 and etc.).
    """
    result = ''

    for number in numbers:
        if number == number[::-1]:
            result += "True\n"
        else:
            result += "False\n"
    return result


digits = input().split(", ")
checked_digits = palindrome_checker(digits)
print(checked_digits)



