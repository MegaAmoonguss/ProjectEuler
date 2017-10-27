from math import sqrt


def factor(n):
    factors = []
    
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n / i:
                factors.append(int(n / i))
            
    return sorted(factors)


def prime_factor(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def factor_sum(n):
    total = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            total += i
            if i != n / i and i != 1:
                total += n / i
    return total


def is_prime(n):
    if n == 1:
        return False
    
    for i in range(2, int(sqrt(abs(n))) + 1):
        if n % i == 0:
            return False
    return True


def is_3_digit_multiple(n):
    factors = factor(n)
     
    for i in range(len(factors)):
        current_factor = factors[i]
        if len(str(current_factor)) == 3 and len(str(int(n / current_factor))) == 3:
            return True 
    return False


def fibonacci(max_value):
    fib = [1, 2]
    i = 1

    while fib[len(fib) - 1] < max_value:
        fib.append(fib[i] + fib[i - 1])
        i += 1
    
    return fib[len(fib) - 2]


def prime_gen(start=2):
    n = start
    while True:
        if is_prime(n):
            yield n
        n += 1


def prime_list(max_value, start=2):
    primes = []
    for n in range(start, max_value + 1):
        if is_prime(n):
            primes.append(n)
    return primes


def calc_day(d, m, y, c):
    return (d + m + y + (y / 4) + c) % 7

def rotations(s):
    rotations = []
    for i in range(len(s)):
        rotations.append(s[-i:] + s[:-i])
    return rotations


def word_value(w):
    return sum([ord(c) - 64 for c in w])


def is_triangle_number(n):
    return sqrt(8 * n + 1) == int(sqrt(8 * n + 1))


def is_pentagon_number(n):
    return (1 + sqrt(24 * n + 1)) / 6 == int((1 + sqrt(24 * n + 1)) / 6)


def is_palindrome(s):
    return s == s[::-1]


def is_truncatable_prime(n):
    if not is_prime(n):
        return False
    
    for i in range(1, len(str(n))):
        num1 = int(str(n)[-i:])
        num2 = int(str(n)[:-i])
        if not (is_prime(num1) and is_prime(num2)):
            return False
    return True


def parse_triangle(triangle):
    return [[int(n) for n in s.split()] for s in triangle.split('\n') if s]
