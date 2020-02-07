import math
import euclid
import sys
import prime

dc = {}
for code in sys.stdin:
    code = code.strip()
    for i in range(len(code)):
        key = int(code[i])
        if key not in dc:
            dc[key] = []

        for val in code[:i]:
            val = int(val)
            if val not in dc[key]:
                dc[key].append(val)

for key in sorted(dc, key=lambda key: len(dc[key])):
    print(key, end='')
print()
