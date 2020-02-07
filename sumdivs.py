import sys

def primef(N):
    div = {}
    v = 2
    while v <= N//v:
        if N % v == 0:
            div[v] = 0
            while N % v == 0:
                div[v] += 1
                N //= v
        v += 1
    if N > 1 and N not in div:
        div[N] = 1
    return div

def sumdivs(N):
    res = 1
    divs = primef(N)
    for p in divs:
        k = divs[p]
        res *= (p**(k+1) - 1)/(p-1)
    return int(res) - N
