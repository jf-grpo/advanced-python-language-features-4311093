# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate the use of lambda functions

# To learn more about docstrings > peps.python.org/pep-0257/

def my_function(arg1, arg2=None):
    # to add a doc funtion
    """
    my_funtion(arg1, arg2=None) --> Doesn't really do anything special.
    Parameters:
    arg1: the first argument.
    arg2: the second argument.
    """
    print(arg1, arg2)


print(my_function.__doc__)
