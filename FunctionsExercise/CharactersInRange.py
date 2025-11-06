def characters_in_given_range(character_one,character_two):
    result = ''
    for character in range(ord(character_one) + 1, ord(character_two)):
        result += chr(character) + ' '
    return result


first_symbol = input()
second_symbol = input()
symbols_in_between = characters_in_given_range(first_symbol,second_symbol)
print(symbols_in_between)