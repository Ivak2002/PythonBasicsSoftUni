number = int(input())
synonyms = dict()
for word in range(number):
    current_word = input()
    synonym = input()
    if current_word not in synonyms:
        synonyms[current_word] = []
    synonyms[current_word].append(synonym)
for word in synonyms:
    print(f"{word} - {', '.join(synonyms[word])}")
