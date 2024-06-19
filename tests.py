def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 2 - 1 == 1

def test_multiplication():
    assert 2 * 2 == 4

def test_division():
    assert 4 / 2 == 2

# Example of a function with a docstring that contains a doctest
def square(x):
    """
    This function returns the square of the given number.

    >>> square(2)
    4
    >>> square(3)
    9
    """
    return x * x
