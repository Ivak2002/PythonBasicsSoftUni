def is_letter(char):
    is_uppercase = 64 < ord(char) < 91
    is_lowercase = 96 < ord(char) < 123

    return is_lowercase or is_uppercase


def is_number(char):
    return 47 < ord(char) < 58


def main():
    length_req = True
    letters_and_digits_req = True
    two_digits_req = True

    pass_in = input()

    length_req = 5 < len(pass_in) < 11
    if not length_req:
        print("Password must be between 6 and 10 characters")

    digit_count = 0
    for x in pass_in:
        is_num = is_number(x)
        is_let = is_letter(x)

        if is_let == False and is_num == False:
            letters_and_digits_req = False

        if is_num:
            digit_count += 1

    if not letters_and_digits_req:
        print("Password must consist only of letters and digits")

    if digit_count < 2:
        print("Password must have at least 2 digits")
        two_digits_req = False

    if length_req and letters_and_digits_req and two_digits_req:
        print("Password is valid")


if __name__ == "__main__":
    main()
