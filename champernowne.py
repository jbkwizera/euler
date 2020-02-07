x = '-'
i = 1
while len(x) < 1000001:
    x += str(i)
    i += 1

p = 1
d = 1
while d <= 1000000:
    p *= int(x[d])
    d *= 10

print(p)
