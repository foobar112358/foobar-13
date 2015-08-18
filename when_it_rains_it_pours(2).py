import copy

__author__ = 'Liam'


def answer(heights):
    if len(heights) < 3:
        return 0
    counter = 0
    reference = copy.copy(heights)
    i = reference.index(max(reference))
    reference[i] = 0

