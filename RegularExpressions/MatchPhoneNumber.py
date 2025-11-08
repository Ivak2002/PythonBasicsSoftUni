import re

text = input()

pattern = r"(?<=\s|^)\+359([ -])2\1\d{3}\1\d{4}\b"

matches = re.findall(pattern, text)  # this returns only delimiter groups!
matches = re.finditer(pattern, text)  # this returns full matches

valid_phones = [m.group(0) for m in matches]
print(", ".join(valid_phones))
