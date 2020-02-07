import timeit
import math
import euclid
import sys
import prime

'''
131 763 234 103  18
201  96 342 965 150
630 803 746 422 111
537 699 497 121 956
805 732 524  37 331
-------------------
'''

a = []
for line in sys.stdin:
    line = line.strip().split(',')
    tem  = [int(x) for x in line]
    a.append(tem)

m = len(a)
n = len(a[0])

for j in range(n-2, -1, -1):
    a[m-1][j] += a[m-1][j+1]

for r in range(m-2, -1, -1):
    a[r][n-1] += a[r+1][n-1]
    for c in range(n-2, -1, -1):
        mn = min(a[r+1][c], a[r][c+1])
        a[r][c] += mn

mn = float('inf')
for j in range(0, n):
    if a[0][j] < mn:
        mn = a[0][j]

print(a[0][0])


#---------------------------------------------

def
