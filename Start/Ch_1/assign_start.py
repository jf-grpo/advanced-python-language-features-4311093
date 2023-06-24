# Example file for Advanced Python: Language Features by Joe Marini
# The assignment expression operator := (or the "walrus" operator)

import pprint


# regular assignment statements assign a value
# x = 5
# print(x)

# TODO: the assignment operator is part of an expression
# the := is known as the "walrus" operator because it looks like eyes and tusks
# the walrus operator assigns a value to a variable as part of an expression
# without and expression, the walrus operator is invalid
# why does this operator exist?
# it helps with the readability of code
# x := 10
# print(x)

# TODO: The assignment expression is useful for writing concise code
# thestr = input("Value? ")
# while thestr != "exit":
#     print(thestr)
#     thestr = input("Value? ")
# with the code above, the variable thestr is assigned twice

# let's simplify this code with the walrus operator
# while (thestr := input("Value? ")) != "exit":
#     print(thestr)
# now we're assigning and performing the check at the same time

# TODO: The walrus operator can help reduce redundant function calls
values = [12, 0, 10, 5, 9, 18, 41, 23, 30, 16, 18, 9, 18, 22]
# val_data = {
#     "length": len(values),
#     "total": sum(values),
#     "average": sum(values) / len(values)
# }
# pprint.pp(val_data)
# the above code works but will be more inefficient as calcuations in
# val_data are more complex
# rather than store values in variables that are only used once, we can use the walrus operator

val_data = {
    "length": (l := len(values)),
    "total": (s := sum(values)),
    "average": s / l
}
pprint.pp(val_data)

# the walrus operator was added in PEP 527
# peps.python.org/pep-0572/
