from euler import is_prime

def calc_layer(layer):
    # top right equation: t_n = 4n^2 - 2n + 1
    # top left equation: t_n = 4n^2 + 1
    # bottom left equation: t_n = 4n^2 + 2n + 1
    # bottom right equation: t_n = 4n^2 + 4n + 1
    
    # list of corners, goes top right, top left, bottom left, bottom right
    corners = []
    
    corners.append((4 * layer**2) - (2 * layer) + 1)
    corners.append((4 * layer**2) + 1)
    corners.append((4 * layer**2) + (2 * layer) + 1)
    corners.append((4 * layer**2) + (4 * layer) + 1)
    
    return corners
            
count = 3
total = 5
layer = 1
while count / total >= 0.1:
    layer += 1
    corners = calc_layer(layer)
    
    for n in corners:
        if is_prime(n):
            count += 1
    total += 4

print(count, '/', total)
print("Length:", 2 * layer + 1)