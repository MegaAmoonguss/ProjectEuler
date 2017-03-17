from math import factorial

total = 0
for n in range(10, 1000001):
    current = 0
    for d in str(n):
        current += factorial(int(d))
    if current == n:
        total += n
        print(n)
        
print(total)