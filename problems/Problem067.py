from euler import parse_triangle

triangle_ex = """
3
7 4
2 4 6
8 5 9 3"""

with open('inputs/p067_triangle.txt') as file:
    parsed_67 = parse_triangle(file.read())


def max_sum(triangle: list) -> int:
    """Returns the max total from top to bottom of the given parsed triangle"""
    if len(triangle) == 1:
        return triangle[0][0]
    else:
        return max(triangle[0][0] + max_sum(triangle_split(triangle)[0]),
                   triangle[0][0] + max_sum(triangle_split(triangle)[1]))


def max_sum_v2(triangle: list) -> int:
    """Returns the max total from top to bottom of the given parsed triangle"""
    if len(triangle) == 1:
        return triangle[0][0]
    else:
        for c in range(len(triangle[-2])):
            triangle[-2][c] = triangle[-2][c] + max(triangle[-1][c], triangle[-1][c + 1])
        return max_sum_v2(triangle[:-1])


def triangle_split(triangle: list) -> list:
    """Returns a list of the two sub triangles of the given triangle"""
    left = []
    right = []
    for r in range(1, len(triangle)):
        left.append(triangle[r][:len(triangle[r]) - 1])
        right.append(triangle[r][1:])

    return [left, right]

print(max_sum_v2(parsed_67))
