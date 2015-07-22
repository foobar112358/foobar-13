__author__ = 'Liam Leahy'

from operator import itemgetter
#Edit file

def answer(meetings):
    """
    >>> answer([[0, 1], [1, 2], [2, 3], [3, 5], [4, 5]])
    4
    >>> answer([[0, 1000000], [42, 43], [0, 1000000], [42, 43]])
    1
    >>> answer([[1, 2], [0, 3], [1, 4], [1, 4], [1, 5], [2, 6], [0, 7], [6, 7]])
    3
    """
    return compute(sorted(meetings, key=itemgetter(1)))


def compute(meetings):
    """
    :param meetings: A list where each element
     is a size-2 list containing the start and
     end time of the meeting in that order.
    :return: The maximum number of non-overlapping
    meetings that you can have from that list
    (in one day). changes
    """
    if len(meetings) == 0:
        return 0
    meeting = meetings.pop(0)
    cont = []
    while len(meetings) > 0 and meetings[0][0] < meeting[1]:
        cont.append(meetings.pop(0))
    return max(compute(meetings) + 1, compute(cont + meetings))
