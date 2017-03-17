from euler import prime_factor

def main():
    found = False
    n = 1
    while not found:
        if len(set(prime_factor(n))) >= 4 and len(set(prime_factor(n + 1))) >= 4 and len(set(prime_factor(n + 2))) >= 4 and len(set(prime_factor(n + 3))) >= 4:
            found = True
        else:
            n += 1
    print(n)
    
if __name__ == '__main__':
    main()