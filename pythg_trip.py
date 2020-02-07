import math
import euclid
import sys
import prime

def pyth(s):
    count = 0
    for x in range(3, (s-3)//3 + 1):
        for y in range(x+1, (s-1-x)//2 + 1):
            z = s - x - y
            if x*x + y*y == z*z:
                count += 1
    return count

def pythmx(s):
    count = 0
    s2  = s//2
    mmx = math.ceil(math.sqrt(s2))
    tem = []
    for m in range(2, mmx):
        if s2 % m == 0:
            sm = s2 //m
            while sm % 2 == 0:
                sm //= 2
            k = m + 1 + m % 2
            while k < 2*m and k <= sm:
                if sm % k == 0 and euclid.gcd(k, m) == 1:
                    d = s2 // (k*m)
                    n = k-m
                    a = d*(m*m - n*n)
                    b = 2*d*m*n
                    c = d*(m*m + n*n)
                    tem.append((a, b, c))
                k += 2
    return tem

if __name__ == '__main__':
    mx = 0
    ms = 0
    for s in range(1000):
        count = pythmx(s)
        if count > mx:
            mx = count
            ms = s

    print(ms, mx)
