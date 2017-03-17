import euler

num = 1
count = 0
while count < 10001:
    num += 1
    if euler.is_prime(num):
        count += 1
print(num)