import copy

__author__ = 'Liam'

def answer(heights):
    """
    >>> answer([1, 4, 2, 5, 1, 2, 3])
    5
    >>> answer([1, 2, 3, 2, 1])
    0
    """
    counter = 0
    ref = copy.copy(heights)
    ran = 0
    j = ref.index(max(ref))
    abs_max = max(heights)
    ref[j] = 0
    i = ref.index(max(ref))
    ran += abs(i - j)
    while ran < (len(heights) - 2):
        counter += fill_in_matrix(ref, i, j)
        i, j = find_max_outside_range(ref, i, j)
        counter += fill_in_matrix(ref, i, j)
    return counter


def find_max_outside_range(ref, i, j):
    """Takes in the reference list and the indices bounding the fill range.
    Modifies reference list to reflect filling and returns new effective range
    indices. 
    """
    ret = ref.index(max(ref))
    if (ret < min(i , j)):
        lg = max(i, j)
    else:
        lg = min(i, j)
    ref[ret] = 0
    return ret, lg


def fill_in_matrix(matrix, i, j):
    """Fills all possible spaces between i, j
    and returns the total number of spaces filled. 
    """
    counter = 0
    maxi = min(matrix[i], matrix[j])
    for k in range(min(i, j) + 1, max(i, j)):
        counter += abs(maxi - matrix[k])
        matrix[k] = 0
    return counter