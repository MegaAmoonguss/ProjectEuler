import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, range(n, n-r, -1))
    denom = reduce(op.mul, range(1, r+1))
    return numer//denom

count = 0
for n in range(1, 101):
    for r in range(1, n):
        if ncr(n, r) > 1000000:
            count += 1
print(count)