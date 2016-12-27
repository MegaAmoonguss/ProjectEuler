total = 2
for _ in range(7830456):
    total *= 2
    total = int(str(total)[-10:])
    
total *= 28433
total = int(str(total)[-10:])
total += 1
    
print(total)