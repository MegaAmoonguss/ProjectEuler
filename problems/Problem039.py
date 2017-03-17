def main():
    max_num = 120
    max_tri = 3
     
    for n in range(121, 1000):
        print(n)
        triangles = num_tri(n)
        if triangles > max_tri:
            max_tri = triangles
            max_num = n
    print(max_num)
        
def num_tri(p):
    count = 0
    triples = []
    for i in range(1, int(p / 2)):
        for j in range(i, int(p / 2)):
            k = p - i - j
            sides = sorted((i, j, k))
            if sides[0]**2 + sides[1]**2 == sides[2]**2 and not contains(sides, triples):
                count += 1
                triples.append(sides)
    return count

def contains(e, l):
    for i in l:
        if i == e:
            return True
    return False
    
if __name__ == '__main__':
    main()