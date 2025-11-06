def filter_even_words(text):
    return [word for word in text if len(word) % 2 == 0]


words = input().split()
result = filter_even_words(words)

for w in result:
    print(w)