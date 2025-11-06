number_of_strings = int(input())
required_word = input()
list_of_all_sentences = []
list_of_filtered_sentences = []

for sentence in range(number_of_strings):
    string = input()
    list_of_all_sentences.append(string)
    if string.__contains__(required_word):
        list_of_filtered_sentences.append(string)
    else:
        continue

print(list_of_all_sentences)
print(list_of_filtered_sentences)