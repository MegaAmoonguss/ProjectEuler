num = 1
max = 0
while num < 1000000:
    total = ''
    for n in range(1, 10):
        if len(total + str(num * n)) > 9:
            break
        else:
            total += str(num * n)
            if len(total) == 9:
                if (('0' not in total) and
                    (len(set(total)) == 9) and
                    (int(total) > max)):
                    max = int(total)
                    print(max)
    num += 2