from euler import prime_list, is_prime
from itertools import permutations

primes = prime_list(9999, 1000)

for p in primes:
    if p == 1487:
        print()
    perms = list(set([int(''.join(n)) for n in permutations(str(p))]))

    for i in range(len(perms)):
        for j in range(i+1, len(perms)):
            difference = abs(perms[i] - perms[j])
            for k in range(j+1, len(perms)):
                if perms[k] == perms[i] + difference or perms[k] == perms[j] + difference:
                    nums = (perms[i], perms[j], perms[k])
                    works = True
                    for n in nums:
                        if not is_prime(n):
                            works = False
                            break
                    if works:
                        print(nums)