from euler import is_prime

max = 0
product = 0
for a in range(-999, 1000):
    for b in range(-999, 1000, 2):
        n = 0
        prime_count = 0
        while is_prime((n**2) + (a * n) + b):
            prime_count += 1
            n += 1
            if prime_count > max:
                product = a * b
                max = prime_count
print(product)