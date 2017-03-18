prev_n = 3
prev_d = 2

count = 0
for _ in range(999):
    n = prev_n + 2 * prev_d
    d = prev_n + prev_d
    prev_n = n
    prev_d = d
    
    if len(str(n)) > len(str(d)):
        count += 1

print(count)