def numberfy(t):
    return int(''.join([str(x) for x in t]))

def permuts(t, a, res):
    if len(t) == 4:
        if numberfy(t[1:]) % 2 != 0:
            return
    if len(t) == 5:
        if numberfy(t[2:]) % 3 != 0:
            return
    if len(t) == 6:
        if numberfy(t[3:]) % 5 != 0:
            return
    if len(t) == 7:
        if numberfy(t[4:]) % 7 != 0:
            return
    if len(t) == 8:
        if numberfy(t[5:]) %11 != 0:
            return
    if len(t) == 9:
        if numberfy(t[6:]) %13 != 0:
            return
    if len(t) ==10:
        if numberfy(t[7:]) %17 != 0:
            return


    if not a:
        res += [t]
    else:
        for i in range(len(a)):
            permuts(t + [a[i]], a[0:i] + a[i+1:], res)
    return res

if __name__ == '__main__':
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sum = 0
    for perm in permuts([], a, []):
        print(numberfy(perm))
        sum += numberfy(perm)
    print(sum)
