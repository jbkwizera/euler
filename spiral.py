import timeit
import math
import euclid
import sys
import prime

count = 1
for j in range(2, 10000):
    n  = 4*j - 3
    so = 2*j - 1
    s2 = 2*(j-1)
    s4 = 4*(j-1)
    s6 = 6*(j-1)
    mr = so ** 2
    ml = mr - s4
    nr = mr - s6
    nl = mr - s2
    #if prime.isprime(ml): count += 1
    #if prime.isprime(nr): count += 1
    #if prime.isprime(nl): count += 1
    #v = count*1.0/n
    #if v < 0.10:
    #    print(n)
    #    break
    count += mr + ml + nr + nl
    if so == 1001:
        print(count)
        break
