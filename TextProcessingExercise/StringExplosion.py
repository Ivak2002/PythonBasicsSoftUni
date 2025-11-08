text = input()
strength = 0
result = ""

for i in range(len(text)):
    if text[i] == ">":
        strength += int(text[i + 1])
        result += ">"
    else:
        if strength > 0:
            strength -= 1
        else:
            result += text[i]

print(result)
