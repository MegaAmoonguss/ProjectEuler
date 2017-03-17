from euler import is_palindrome

total = 0
for n in range(1000000):
    if is_palindrome(str(n)) and is_palindrome(str(bin(n))[2:]):
        total += n
print(total)