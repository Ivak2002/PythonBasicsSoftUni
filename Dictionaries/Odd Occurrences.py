string_sequence = map(lambda letter:letter.lower(),input().split())
string_dictionary = dict()
occurrence_times = 1
# input : Java C# PHP PHP JAVA C java
for string in string_sequence:

    if string not in string_dictionary.keys():
        string_dictionary[string] = occurrence_times
    else:
        string_dictionary[string] += 1
string_of_odds = ""
for key in string_dictionary.keys():
    if string_dictionary[key] % 2 != 0:
        string_of_odds += key + " "
print(string_of_odds)
