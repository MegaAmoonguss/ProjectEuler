from euler import is_prime, rotations, prime_list

circular_primes = []
primes = prime_list(1000000)
for p in primes:
    print(p)
    rots = rotations(str(p))
    circular = True
    for r in rots:
        if not is_prime(int(r)):
            circular = False
    if circular:
        circular_primes.append(p)

print(len(circular_primes))
print(circular_primes)