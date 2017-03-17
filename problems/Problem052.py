def get_digits(n):
    return sorted(list(str(n)))

x = 1
while True:
    if get_digits(x) == get_digits(2 * x) == get_digits(3 * x) == get_digits(4 * x) == get_digits(5 * x) == get_digits(6 * x):
        print(x)
        break
    x += 1