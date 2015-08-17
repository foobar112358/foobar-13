__author__ = 'Liam'

def answer(heights):
    """
    >>> answer([1, 4, 2, 5, 1, 2, 3])
    5
    >>> answer([1, 2, 3, 2, 1])
    0
    """
    changed = True
    counter = 0
    matrix, maxi = configure_matrix(heights)
    while changed:
        changed = False
        for i in range(len(matrix) - 1):
            i += 1
            for j in range(maxi):
                if (check_possible(matrix, i, j)):
                    matrix[i][j] = 'w'
                    counter += 1
                    changed = True
    return counter


def configure_matrix(heights):
    matrix = [[None for _ in range(max(heights))] for _ in range(len(heights))]
    maxi = max(heights)
    for i in range(len(heights)):
        for j in range(maxi):
            if j < heights[i]:
                matrix[i][j] = 'b' #'b' for brick
            else:
                matrix[i][j] = 'p' #'p' for potential
    return matrix, maxi

def check_possible(matrix, i, j):
    if (matrix[i][j] == 'p'):
        if (matrix[i][j-1] == 'b' or matrix[i][j-1] == 'w'):
            if (matrix[i-1][j] == 'b' or matrix[i-1][j] == 'w'):
                if (matrix[i+1][j] == 'b' or matrix[i+1][j] == 'w'):
                    return True
    return False