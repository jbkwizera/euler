
def sieve(N):
    isprime = [True]*(N + 2)
    i = 2
    while i <= N//i:
        if isprime[i]:
            for j in range(i, N//i + 1):
                isprime[i*j] = False
        i += 1
    return isprime

def gcd(p, q):
    if q == 0:
        return p
    return gcd(q, p % q)

def isprime(p):
    a = sieve(p)
    return a[p]

import sys
if __name__ == '__main__':
    print(isprime(int(sys.argv[1])))
