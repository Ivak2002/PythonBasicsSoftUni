characters_list = input().split(", ")
characters_dict = dict()
for character in characters_list:
    character_as_char = ord(character)
    characters_dict[character] = character_as_char
print(characters_dict)
