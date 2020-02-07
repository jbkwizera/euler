def partitions(n, I=1):
    yield (n,)
    for i in range(I, n//2 + 1):
        for p in partitions(n-i, i):
            yield (i,) + p

import sys


n = int(sys.argv[1])
x = 1
num = 1
den = 1
for i in range(n):
    #x = 1 + 1.0/(1 + x)
    tem = num
    num += 2*den
    den += tem


print(num*1.0/den, 2**0.5)
