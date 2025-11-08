sub = input()
text = input()

while sub in text:
    text = text.replace(sub, "")

print(text)
