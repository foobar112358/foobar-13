__author__ = 'Liam Leahy'


def fizzbuzz():
    """
    >>> fizzbuzz()
    """
    x = 100
    for i in range(x):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)
