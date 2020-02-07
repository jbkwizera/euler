import prime

N = 1000000;
isprime = prime.sieve(N)

primesum = 0
sum = 0
cur = 0
max = 0
for v in range(2, 1000):
    if sum > 1E6:
        break
    if isprime[v]:
        sum += v
        cur += 1
        if isprime[sum]:
            if cur >= max:
                primesum = sum
                max = cur
            cur = 0
print(primesum)
