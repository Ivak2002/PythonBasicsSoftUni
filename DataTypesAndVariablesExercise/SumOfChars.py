numbers_of_chars = int(input())
result = 0
for char in range(numbers_of_chars):
    character = input()
    current_char_ascii_number = ord(character)
    result += current_char_ascii_number
print(f"The sum equals: {result}")
