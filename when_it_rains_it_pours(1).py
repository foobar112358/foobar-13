import copy, heapq

__author__ = 'Liam'


def answer(heights):
    """
    >>> answer([1, 4, 2, 5, 1, 2, 3])
    5
    >>> answer([1, 2, 3, 2, 1])
    0
    >>> answer([2,2,2,2,2,2,2,2])
    0
    >>> answer([1,2,3,3,2,3,4,5,6])
    1
    >>> answer([0])
    0
    >>> answer([1,2,3,4,5,6,7,8,7,9])
    1
    >>> answer([1,2,1,2,1,2,1,2,1])
    3
    """
    if len(heights) <= 2 or all_same(heights):
        return 0
    counter = 0
    i = heights.index(max(heights))
    max_val = heights[i]
    j = get_other(heights, i)
    counter += fill_in_matrix(heights, i, j)
    return counter + answer(heights[:min(i, j) + 1]) + answer(heights[max(i, j):])


def fill_in_matrix(matrix, i, j):
    """Fills all possible spaces between i, j
    and returns the total number of spaces filled. 
    """
    counter = 0
    maxi = min(matrix[i], matrix[j])
    for k in range(min(i, j) + 1, max(i, j)):
        counter += abs(maxi - matrix[k])
    return counter


def all_same(heights):
    i = heights[0]
    for j in heights:
        if i != j:
            return False
    return True


def get_other(heights, i):
    ref = copy.copy(heights)
    ref[i] = 0
    return ref.index(max(ref))
