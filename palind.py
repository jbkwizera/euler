import sys

def ersever(n):
    m = 0
    while n > 0:
        m = 10 * m + n % 10
        n = n // 10
    return m

def ispalind(n):
    return n == ersever(n)

def deluxe(d):
    m = 10**d
    n = m//10

    mx = 0
    for x in range(m-1, n-1, -1):
        if x % 11 == 0:
            for y in range(m-1, x-1, -1):
                v = x * y
                if v <= mx: break
                if ispalind(v):
                    mx = v
        else:
            for y in range(m-10, x-1, -11):
                v = x * y
                if v <= mx: break
                if ispalind(v):
                    mx = v
    return mx

def evpalind(d):
    m = 10**d
    n = m//10

    mx = 0
    for x in range(m-1, n-1, -1):
        for y in range(m-1, x-1, -1):
            v = x * y
            if v <= mx: break
            if ispalind(v):
                mx = v
    return mx

if __name__ == '__main__':
    d = 3
    if len(sys.argv) > 1:
        d = int(sys.argv[1])

    for i in range(1, 6):
        frmt = '{:>1d} {:>14d} {:>14d}'
        print(frmt.format(i, evpalind(i), deluxe(i)))
