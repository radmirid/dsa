import sys
import re

s = 0

for line in sys.stdin:
    for match in re.finditer(r'-?\d+', line):
        start, end = match.start(), match.end()
        s += int(line[start:end])

print(s)
