from euler import is_prime
from euler import prime_list

sum = 0
max = 0
primes = prime_list(1000)
for p in primes:
    if sum + p >= 1000:
        break
    sum += p
    if is_prime(sum):
        max = sum



print(max)