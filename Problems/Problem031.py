def main():
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    num_coins = [1, 0, 0, 0, 0, 0, 0, 0]
    
    count = 1
    for i in range(len(num_coins)):
        while True:
            total = 0
            for j in range(len(num_coins)):
                total += num_coins[j] * coins[j]
            
            if total == 200:
                count += 1
                num_coins -= 1
                break
            elif total < 200:
                num_coins[i] += 1
            else:
                num_coins[i] -= 1
                break
    
if __name__ == '__main__':
    main()