text = input()

for i in range(len(text) - 1):
    if text[i] == ":":
        print(text[i:i+2])
