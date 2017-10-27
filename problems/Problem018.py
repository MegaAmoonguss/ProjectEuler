from euler import parse_triangle

triangle_ex = """
3
7 4
2 4 6
8 5 9 3"""

triangle_18 = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


def brute_force_max(triangle):
    """Returns the max total from top to bottom of the given parsed triangle"""
    max_sum = 0

    # Use a bitstring to represent going left or right down the triangle (0 = left, 1 = right)
    for path_num in range(2**(len(triangle) - 1)):
        path_bits = bin(path_num)[2:]
        path_bits = '0' * (len(triangle) - len(path_bits) - 1) + path_bits

        total = triangle[0][0]
        column = 0
        for row in range(1, len(triangle)):
            if int(path_bits[row - 1]):
                column += 1
                total += triangle[row][column]
            else:
                total += triangle[row][column]

        if total > max_sum:
            max_sum = total

    return max_sum


parsed_18 = parse_triangle(triangle_18)
print(brute_force_max(parsed_18))
