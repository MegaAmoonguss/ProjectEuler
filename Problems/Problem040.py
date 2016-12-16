def main():
    s = ''
    product = 1
    
    n = 1
    while len(s) <= 1000000:
        s += str(n)
        n += 1
    
    i = 1
    while i <= 1000000:
        product *= int(s[i - 1])
        i *= 10
    print(product)
    
if __name__ == '__main__':
    main()