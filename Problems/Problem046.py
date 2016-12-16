from euler import is_prime, prime_list
from math import sqrt

def main():
    start = 200
    global primes
    primes = prime_list(start)
    n = 33
    
    while True:
        n += 2
        if n > primes[len(primes) - 1]:
            primes += prime_list(n, start)
            start = n
        if not is_prime(n) and not goldbach(n):
            break
    print(n)

def goldbach(n):
    for p in primes:
        if p > n:
            break
        else:
            test = sqrt((n - p) / 2)
            if test == int(test):
                return True
    return False
        
if __name__ == '__main__':
    main()