#import module to solve the pylint print error
from __future__ import print_function
def smart_divide(func):
    """The function's docstring"""
    def inner(var1, var2):
        """The function's docstring"""
        print("I am going to divide", var1, "and", var2)
        if var2 == 0:
            return "Whoops! cannot divide"
        return func(var1, var2)
    return inner


@smart_divide
def divide(var1, var2):
    """The function's docstring"""
    print(var1/var2)

print(divide(2, 0))
