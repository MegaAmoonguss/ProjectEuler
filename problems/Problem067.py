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


with open('inputs/p067_triangle.txt') as file:
    parsed_67 = parse_triangle(file.read())


def max_sum(triangle: list) -> int:
    """Returns the max total from top to bottom of the given parsed triangle"""
    if len(triangle) == 1:
        return triangle[0][0]
    else:
        return max(triangle[0][0] + max_sum(triangle_split(triangle)[0]),
                   triangle[0][0] + max_sum(triangle_split(triangle)[1]))


def triangle_split(triangle: list) -> list:
    """Returns a list of the two sub triangles of the given triangle"""
    left = []
    right = []
    for r in range(1, len(triangle)):
        left.append(triangle[r][:len(triangle[r]) - 1])
        right.append(triangle[r][1:])

    return [left, right]

parsed_18 = parse_triangle(triangle_18)
print(max_sum(parsed_18))
