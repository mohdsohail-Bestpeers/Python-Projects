"""import module to solve the pylint print error"""
from __future__ import print_function


def decor(result_function):
    """Decorator function"""

    def distinction(marks):
        """Inner function"""
        for mark in marks:
            if mark >= 75:
                print("You Got Distinction")
        return result_function(marks)

    return distinction


@decor
def result(marks):
    """Main function"""
    for mark in marks:
        if mark >= 33:
            pass
        else:
            print("FAIL")
            break
    else:
        print("PASS")


result([33, 35, 34, 35, 34])
