def main():
    products = set()
    
    total = 0
    for i in range(99):
        for j in range(9877):
            if i > 9 and j > 999:
                break
            p = i * j
            nums = str(i) + str(j) + str(p)
            if len(nums) == len(set(nums)) and len(nums) == 9 and not '0' in nums and not p in products:
                total += p
                products.add(p)
    print(total)
    
if __name__ == '__main__':
    main()