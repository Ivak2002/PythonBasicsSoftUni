def removing_vowels(text):
    """
    This function takes a string(text) and removes all the vowels.
    """
    text_two = ''
    vowels = ['a', 'e', 'i', 'o', 'u']

    for symbol in text:
        if not symbol.lower() in vowels:
            text_two += symbol

    return text_two


text_input = input()
new_text = removing_vowels(text_input)
print(new_text)
