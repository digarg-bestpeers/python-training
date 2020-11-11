"""Extend functionality of a function using decorator"""


def decorator_function(main_function_as_argument):
    """Decorator function declaration"""

    def inner_function():
        number1 = main_function_as_argument()
        result = number1 + 5
        return result

    return inner_function


@decorator_function  # extended functionality using decorator function
def main_function():
    """Main function declaration"""
    return 10


print(main_function())
print(main_function.__name__)
