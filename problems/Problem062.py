def smallest_cube(n: int) -> int:
    """Finds the smallest cube for which exactly n permutations of its digits are cube"""
    count = 0
    found = False
    while not found:
        
