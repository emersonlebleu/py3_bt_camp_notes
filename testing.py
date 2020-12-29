#---Notes: Testing---#

#TDD: Test Driven Development (Red, Green, Refactor)
#this is different from testing because you write your tests first (is the minority)

#---Assertions---# not the end all be all of testing
#--Example--
def add_positive_numbers(x, y):
    assert x > 0 and y > 0, "Both numbers must be positive." #here it is
    return x + y
#if a python file is run with the -O flag, assertions will be ignored

#---Doctests---#
#work as both documentation and as a test that python can execute
def add(a, b):
    """performs addition on two numeric values, can also function for strings
    >>> add(2,3)
    5
    >>> add(100,200)
    300
    >>> add('llama','llama')
    'llamallama'
    """
    return a + b

#syntax to call: python -m doctest -v file_name.py

def double(values):
    """ double the values in some list (values)
    >>> double([2,3,4,5,6])
    [4, 6, 8, 10, 12]
    >>> double([])
    []
    >>> double(['lol', 'gah'])
    ['lollol', 'gahgah']
    >>> double([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
    """
    #had to correct the type error from the output after failing once for the traceback
    return [val+val for val in values]

#---Unit Test---#
#most popular and many features 
#the idea of unit testing is that you can test individual pieces (units)
#can test, classes, modules, or functions (not really intended for entire applications)

#--will test in unit_test.py--#
def eat(food, is_healthy):
    if not isinstance(is_healthy, bool):
        raise ValueError("is_healthy must be a boolean")
    ending = "because YOLO!"
    if is_healthy == True:
        ending = "because it is healthy."
    return f"I'm eating {food}, {ending}"

#there are a few assertions that we can work with see python documentation for all