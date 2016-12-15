from math import sqrt

def main():
    nums = triangle_nums()
    n = next(nums)
    while (1 + sqrt(24 * n + 1)) / 6 != int((1 + sqrt(24 * n + 1)) / 6) or (1 + sqrt(8 * n + 1)) / 4 != int((1 + sqrt(8 * n + 1)) / 4):
        n = next(nums)
    print(n)
    
def triangle_nums():
    n = 571
    while True:
        yield int((n * (n + 1)) / 2)
        n += 1

if __name__ == '__main__':
    main()