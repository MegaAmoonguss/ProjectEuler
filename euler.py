from math import sqrt

# Methods
def factor(n):
    factors = []
    
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(int(n / i))
            
    return sorted(factors)

def is_prime(n):
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

def prime_list(max_value):
    for n in range(2, max_value + 1):
        if is_prime(n):
            yield n

def calc_day(d, m, y, c):
    return (d + m + y + (y / 4) + c) % 7

def rotations(s):
    rotations = []
    for i in range(len(s)):
        rotations.append(s[-i:] + s[:-i])
    return rotations