from euler import word_value, is_triangle_number

with open('Inputs\p042_words.txt') as file:
    words = [w[1:-1] for w in file.read().split(',')]

count = 0
for w in words:
    if is_triangle_number(word_value(w)):
        count += 1
print(count)