year = int(input())

while True:
    year += 1
    is_happy_year = True
    already_found_digit = ""

    for letter in str(year):
        if letter in already_found_digit:
            is_happy_year = False
            break
        already_found_digit += letter

    if is_happy_year:
        break

print(year)







