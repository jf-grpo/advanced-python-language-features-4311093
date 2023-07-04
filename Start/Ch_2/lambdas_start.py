# Example file for Advanced Python: Language Features by Joe Marini
# Use lambdas as in-place functions


def celsisus_to_fahrenheit(temp):
    return (temp * 9/5) + 32


def fahrenheit_to_celsisus(temp):
    return (temp-32) * 5/9


ctemps = [0, 12, 34, 100]
ftemps = [32, 65, 100, 212]

# TODO: Use regular functions to convert temps
print(list(map(fahrenheit_to_celsisus, ftemps)))
print(list(map(celsisus_to_fahrenheit, ctemps)))

# lambdas are very useful when you don't really need a named function \
# just to execute a simple calculation


# TODO: Use lambdas to accomplish the same thing
# Here is what line 17 would look like using a lambda
# notice the function is now inline as lambda
# t is the parameter, you could use any name
print(list(map(lambda t: (t-32) * 5/9, ftemps)))
# Likewise, here is line 18 using a lambda
print(list(map(lambda t: (t * 9/5) + 32, ctemps)))

# Otherwise you might end up calling functions from other libraries \
# just to do a simple calculation. Down the road one would have to \
# trace back all of those functions to see what they do. \
# This simplifies the code and makes it easier to read.

# They are not ideal for every situation, but they are very useful \
# to keep code simple.
