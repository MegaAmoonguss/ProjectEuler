from euler import is_pentagon_number

def main():
    pents = [int((n * (3 * n - 1)) / 2) for n in range(1, 10000)]
    
    for i in range(len(pents)):
        for j in range(i, len(pents)):
            if is_pentagon_number(pents[i] + pents[j]) and is_pentagon_number(abs(pents[i] - pents[j])):
                print(pents[i], pents[j], abs(pents[i] - pents[j]))
                exit()
    
if __name__ == '__main__':
    main()