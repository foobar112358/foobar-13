__author__ = 'Liam Leahy'

def test():
    """
    >>> test()
    """
    lst = []
    for i in range(13):
        lst.append(calc(i))
    return lst


def calc(x):
    """
    Returns the expectation for getting anywhere from 0 to x points.
    >>> round(calc(1), 4)
    1.0
    >>> round(calc(2), 4)
    1.2259
    >>> calc(13)
    5.6377415993937143
    """
    total = 0
    for i in range(x + 1):
        lst = helper(i)
        ret = 1
        for el in lst:
            ret *= el
        total += ret
    return total

def helper(x):
    """
    >>> helper(1)
    [1]
    >>> helper(2)
    [1.0, 0.94117647058823528, 0.12, 2]
    >>> helper(3)
    [1.0, 0.94117647058823528, 0.88, 0.18367346938775511, 3]
    """
    if x == 0:
        return [0]
    deck_size = 52.0
    lst = []
    table = 0
    numer = deck_size
    for i in range(x):
        numer = (deck_size - (3 * table))
        frac = numer / deck_size
        table += 1
        deck_size -= 1
        lst.append(frac)
    rest_in_deck = 3 * x
    end = rest_in_deck / deck_size
    lst.append(end)
    lst.append(x)
    return lst