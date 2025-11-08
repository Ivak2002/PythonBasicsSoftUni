text = input()
result = text[0]

for ch in text[1:]:
    if ch != result[-1]:
        result += ch

print(result)
