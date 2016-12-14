from euler import is_prime
from itertools import permutations

perms = iter(permutations(('1', '2', '3', '4', '5', '6', '7')))

max = 0
try:
    while True:
        num = int(''.join(next(perms)))
        if is_prime(num) and num > max:
            max = num
except:
    print(max)
