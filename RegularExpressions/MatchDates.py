import re

text = input()

pattern = r"\b(?P<day>\d{2})([.\-/])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b"

matches = re.finditer(pattern, text)

for m in matches:
    print(f"Day: {m.group('day')}, Month: {m.group('month')}, Year: {m.group('year')}")
