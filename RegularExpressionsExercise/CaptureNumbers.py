import re
import sys

pattern = r"\d+"
numbers = []

for line in sys.stdin:
    line = line.strip()
    matches = re.findall(pattern, line)
    numbers.extend(matches)

print(" ".join(numbers))
