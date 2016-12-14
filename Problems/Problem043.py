import itertools

def main():
    perms = iter(itertools.permutations(('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')))
    
    total = 0
    for _ in range(3628800):
        num = ''.join(next(perms))
        if len(num) == 10 and check(num):
            total += int(num)
    print(total)

def check(n):
    if int(n[1:4]) % 2 == 0 and int(n[2:5]) % 3 == 0 and int(n[3:6]) % 5 == 0 and int(n[4:7]) % 7 == 0 and int(n[5:8]) % 11 == 0 and int(n[6:9]) % 13 == 0 and int(n[7:10]) % 17 == 0:
        return True
    return False

if __name__ == '__main__':
    main()