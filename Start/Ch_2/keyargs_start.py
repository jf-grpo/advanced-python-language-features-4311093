# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate the use of keyword-only arguments


# use keyword-only arguments to help ensure code clarity
# essentially force the caller to supply the arguments by name \
# so that it is more clear what the code is doing


# TODO: define a function that uses keyword-only arguments
# everything after the '*' requires use of the keyword
def MyFunction(arg1, arg2, *, suppressExceptions=False):
    pass


# try to call the function without the keyword
# myFunction(1, 2, True)
# MyFunction(1, 2, True) # this will fail \
# stating that 'MyFunction() takes 2 positional arguments \
# but 3 were given'.

# The correct way
MyFunction(1, 2, suppressExceptions=True)  # this will work
