import timeit
import math
import sys

def sumdivs(n):
    sum = 0
    nsq = int(math.sqrt(n))
    for v in range(1, nsq + 1):
        if n % v == 0:
            if n // v == v or v == 1:
                sum += v
            else:
                sum += v + n//v
    return sum

def sumdivv(n):
    N = n
    res = 1
    v = 2
    while v <= n//v:
        p = 1
        while n % v == 0:
            p = p*v + 1
            n //= v
        res *= p
        v += 1
    if n > 1:
        res *= (n + 1)
    return res - N

s1 = '''\
import math
def sumdivs(n):
    sum = 0
    nsq = int(math.sqrt(n))
    for v in range(1, nsq + 1):
        if n % v == 0:
            if n // v == v or v == 1:
                sum += v
            else:
                sum += v + n//v
    return sum

def main():
    lim = 28123
    abd = []
    sum = 0
    for n in range(2, lim+1):
        for u in range(1, n//2 + 1):
            v = n - u
            if sumdivs(u) > u and sumdivs(v) > v:
                break
        else:
            sum += n
    return sum
main()
'''

if __name__ == '__main__':
    lim = int(sys.argv[1])
    T1 = timeit.timeit(stmt=s1, number=1)
    print(T1)
