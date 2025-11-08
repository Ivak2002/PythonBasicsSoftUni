import re

text = input().upper()
pairs = re.findall(r"(\D+)(\d+)", text)

result = ""

for word, num in pairs:
    result += word * int(num)

unique = len(set(result))

print(f"Unique symbols used: {unique}")
print(result)
