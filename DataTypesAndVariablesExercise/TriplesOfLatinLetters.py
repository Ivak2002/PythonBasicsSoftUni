number_of_letters = int(input())
for letter in range(number_of_letters):
    for next_letter in range(number_of_letters):
        for final_letter in range(number_of_letters):
            print(f"{chr(97 + letter)}{chr(97 + next_letter)}{chr(97 + final_letter)}")