from euler import prime_gen, is_truncatable_prime

def main():
    primes = prime_gen(11)
     
    sum = 3797
    count = 1
    while count < 11:
        p = next(primes)
        if is_truncatable_prime(p) and p != 3797:
            print(p)
            sum += p
            count += 1
    print(sum)
    
if __name__ == '__main__':
    main()