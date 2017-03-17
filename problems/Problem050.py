from euler import is_prime, prime_list

primes = prime_list(200000)
print('Primes calculated.')

max = 0
num_terms = 0
for j in range(len(primes)):
    for i in range(len(primes)):
        if i + j == len(primes):
            break
        total = sum(primes[i:i+j])
        if total >= 1000000:
            break
        
        if total % 2 == 1 and is_prime(total):
            num_terms = j
            max = total
            max_range = primes[i:i+j]

print(num_terms, 'terms')
print(max, 'total')