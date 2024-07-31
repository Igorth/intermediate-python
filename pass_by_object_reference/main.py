# Immutable Objects: 
# For IMMUTABLE objects (like integers, strings, and tuples),
# it behaves like PASS-BY-VALUE. The function receives a COPY of the reference,
# but since the object is IMMUTABLE, it CANNOT be modified.
def modify_immutable(x):
    x = x + 1
    print(f"Inside function: {x}")

a = 10
modify_immutable(a)
print(f"Outside function: {a}")

#Mutable Objects: 
# For MUTABLE objects (like lists, dictionaries, and sets),
# it behaves like PASS-BY-REFERENCE. The function receives a REFERENCE to the 
# same object, ALLOWING modifications to the object itself.
def modify_mutable(lst):
    lst.append(4)
    print(f"Inside function: {lst}")

my_list = [1, 2, 3]
modify_mutable(my_list)
print(f"Outside function: {my_list}")

#Summary
# Immutable objects: Changes inside the function do not affect the original object.
# Mutable objects: Changes inside the function affect the original object.