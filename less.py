import timeit

import sys
import math
import euclid
import prime

# you can use logarithms
def less(m, p, n, q):
    if n == 1 or q == 0: return m < 1
    if m == 1 or p == 0: return n > 1
    if p == q:  return m < n
    if m == n:  return p < q
    if p >  q and m > n: False
    if p <  q and m < n: True

    if p >  q:
        n = n / (m**(p//q))
        p = p % q
    else:
        m = m / (n**(q//p))
        q = q % p
    return less(m, p, n, q)

# read lines on stdin
nums = [line.strip() for line in sys.stdin]

mxm = 1
mxp = 1
mxl = 0
for i in range(len(nums)):
   curr = nums[i].split(',')
   m, p = int(curr[0]), int(curr[1])
   if less(mxm, mxp, m, p):
       mxm = m
       mxp = p
       mxl = i

print(mxl+1)
