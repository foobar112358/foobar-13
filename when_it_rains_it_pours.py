import copy

__author__ = 'Liam'


def answer(heights):
    """
    # >>> answer([1, 4, 2, 5, 1, 2, 3])
    # 5
    >>> answer([1, 2, 3, 2, 1])
    0
    """
    ref = copy.copy(heights)
    counter = 0
    maxi = max(heights)
    i = ref.index(max(ref))
    ref[i] = 0
    j = ref.index(max(ref))
    ref[j] = 0
    ran = abs(i - j)
    counter += fill_in_matrix(heights, i, j)
    while ran < (len(heights) - 2):
        x, lg = find_max_outside_range(ref, i, j)
        if x == i:
            i = x
        else:
            j = x
        counter += fill_in_matrix(heights, x, lg)
        ran += abs(lg - x)
    return counter


def fill_in_matrix(matrix, i, j):
    counter = 0
    maxi = min(matrix[i], matrix[j])
    for k in range(min(i, j) + 1, max(i, j)):
        counter += abs(maxi - matrix[k])
    return counter


def find_max_outside_range(ref, i, j):
    ret = ref.index(max(ref))
    if (ret < min(i , j)):
        lg = min(i, j)
    else:
        lg = max(i, j)
    for _ in range(ret, lg):
        ref[_] = 0
    return ret, lg


def configure_matrix(heights):
    matrix = [[None for _ in range(max(heights))] for _ in range(len(heights))]
    maxi = max(heights)
    for i in range(len(heights)):
        for j in range(maxi):
            if j < heights[i]:
                matrix[i][j] = 'b'  # 'b' for brick
            else:
                matrix[i][j] = 'p'  # 'p' for potential
    return matrix, maxi

