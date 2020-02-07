import sys
import math

d = dict()
for v in range(9, 2, -1):
    d[v] = [[x, v-x] for x in range(1, math.ceil(v/2))]

for k in range(9, 2, -1):
    for l in range(k-1, 2, -1):
        for m in range(l-1, 2, -1):
            for x in d[k]:
                for y in d[l]:
                    for z in d[m]:
                        lk = x + [k]
                        ll = y + [l]
                        lm = z + [m]
                        s  = set(lk + ll + lm)
                        if len(s) == 9 and sum(s) == 45:
                            print('found: ', lk, ll, lm)
                        #print('\t', sorted(lk), sorted(ll), sorted(lm), 'sum: ', sum(lk + ll + lm))


def perm(ls, res, tem):
    N = len(ls)
    if N == 0:
        res.append(tem)
    else:
        for i in range(N):
            _tem = tem + [ls[i]]
            _ls  = ls[:i] + ls[i+1:]
            perm(_ls, res, _tem)

def perms(ls):
    res = []
    perm(ls, res, [])
    return res

a = [x for x in range(1, 10)]
r = perms(a)

for T in r:
    for c in range(2, 9, 3):
        if T[c] != T[c-1] + T[c-2]:
            break
    else:
        print(T)
