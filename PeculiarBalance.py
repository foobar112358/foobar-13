__author__ = 'Liam Leahy'
import math

def answer(x):
    """
    :rtype : list
    :param x: Weight on left-hand side of scale.
    :return: List containing strings where the i'th element of the list represents
    the i'th power of 3 and "L" represents putting said power of 3 to the left on
    the scale, "R" for right, and "-" for neither.
    >>> answer(6056)
    ['L', '-', 'R', 'L', '-', 'R', 'L', '-', 'R']
    >>> answer(2)
    ['L', 'R']
    >>> answer(3)
    ['-', 'R']
    >>> answer(8)
    ['L', '-', 'R']
    """
    x -= 1
    div = x
    rem = x
    rems = []
    while not (div == 0 and rem == 0):
        rem = div % 3
        div = (int)(div / 3)
        rems.append(rem)
        if rem == 0 and not (div == 0):
            div -= 1
    ret = []
    for el in rems:
        if el == 0:
            ret.append("R")
        elif el == 2:
            ret.append("-")
        else:
            ret.append("L")
    return ret




def cycle(x, lst):
    return 0


def findLowest(x):
    """
    :rtype : int
    :param x: Integer for which we are
    trying to determine which power of 3
    is the first that is greater than it.
    :return: The first power of three that
    is greater than x.
    """
    i = 0
    ret = 1
    while ret <= x:
        ret = pow(x, i)
        i += 1
    return ret, i


def findGreatest(x):
    """
    :rtype : int
    :param x: The integer that we want to find
    the greatest power of three that is less than or
    equal to x.
    :return: The greatest power of 3 less than or
    equal to x.
    """
    i, j = findLowest(x)
    return i / 3, j - 1


def baseThree(x):
    """
    :type x: int
    :rtype : list
    :param x: Positive integer to be converted to base three.
    :return: A list containing the values required to express x
    in powers of three.
    >>> baseThree(3)
    [3]
    >>> baseThree(6)
    [3, 3]
    >>> baseThree(11)
    [1, 1, 9]
    """
    if x == 0:
        return list()
    i = 1
    while i < x:
        i *= 3
    if i != x:
        i /= 3
    lst = baseThree(x - i)
    lst.append(int(i))
    return lst


