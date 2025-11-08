import re
import sys

pattern = r"\bwww\.[A-Za-z0-9-]+(\.[a-z]+)+\b"

for line in sys.stdin:
    matches = re.findall(pattern, line)
    # Need the full match, so use finditer:
    for m in re.finditer(pattern, line):
        print(m.group(0))
