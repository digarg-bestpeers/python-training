"""Use of method decorator"""


def check_name(method):
    """Decorator function declaration"""

    def inner(name_ref):
        if name_ref.name == "Dinesh":
            print("Hey {}.. my another name is also same!!".format(name_ref.name))
        else:
            method(name_ref)

    return inner


class Printing:
    """Printing class declaration"""

    def __init__(self, name):
        self.name = name

    @check_name
    def print_name(self):
        """Print name method declaration"""
        print("Entered name is: ", self.name)


PRINT_OBJ1 = Printing("Dinesh")
PRINT_OBJ2 = Printing("Garg")

PRINT_OBJ1.print_name()
PRINT_OBJ2.print_name()
