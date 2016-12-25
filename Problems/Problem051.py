from euler import is_prime

num = 121313

while True:
    p = str(num)
    print(p)
    backup = p
    for i in range(len(p) - 1):
        for j in range(i + 1, len(p) - 1):
            s = p[:i] + '*' + p[i+1:]
            s = s[:j] + '*' + s[j+1:]
            print(s)
            
            count = 0
            smallest = 0
            smallest_found = False
            for n in range(10):
                if n == 0 and i == 0:
                    continue
                p = p[:i] + str(n) + p[i+1:]
                p = p[:j] + str(n) + p[j+1:]
                if is_prime(int(p)):
                    count += 1
                    if not smallest_found:
                        smallest = p
                    smallest_found = True
                p = backup
                if n - count == 2:
                    break
                
            if count == 8:
                print('FOUND:', smallest)
                exit()
    num += 2
    break