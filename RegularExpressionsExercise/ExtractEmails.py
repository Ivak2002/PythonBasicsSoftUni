import re

text = input()

pattern = r"\b(?<![._-])[A-Za-z0-9]+(?:[._-][A-Za-z0-9]+)*@[A-Za-z]+(?:-[A-Za-z]+)*(?:\.[A-Za-z]+(?:-[A-Za-z]+)*)+\b"

matches = re.findall(pattern, text)

for email in matches:
    print(email)
