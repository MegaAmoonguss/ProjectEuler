from euler import factor_sum

def main():
    global abundants
    abundants = [n for n in range(28123) if factor_sum(n) > n]
    print(abundants)
    nums = working_nums(abundants)
    
    total = 0
    for i in range(len(nums)):
        if not nums[i]:
            total += i
    print(total)
    
def working_nums(l):
    nums = [False for _ in range(28124)]
    count = 0
    for i in range(len(l)):
        for j in range(i, len(l)):
            count += 1
            sum = abundants[i] + abundants[j]
            if sum <= 28123:
                nums[sum] = True
            else:
                break
    print(count)
    return nums

def is_sum(n):
    n_odd = n % 2 == 1
    for i in range(len(abundants)):
        i_odd = i % 2 == 1
        for j in range(i, len(abundants)):
            if n_odd and i_odd and j % 2 == 0:
                continue
            if abundants[i] + abundants[j] > n:
                break
            elif n == abundants[i] + abundants[j]:
                return True
    return False
    
if __name__ == '__main__':
    main()