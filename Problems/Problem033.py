product = 1

for numerator in range(10, 100):
    for denominator in range(10, 100):
        if '0' in str(denominator):
            continue
        if ((numerator / denominator == int(str(numerator)[0]) / int(str(denominator)[1]) or
            numerator / denominator == int(str(numerator)[1]) / int(str(denominator)[0])) and
            str(numerator)[0] != str(numerator)[1] and
            (str(numerator)[0] == str(denominator)[1] or 
             str(numerator)[1] == str(numerator)[0])):
            product *= denominator / numerator
print('Decimal =', product)