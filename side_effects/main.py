import copy

# Shallow copy
# Creates a new objecct but inserts references into it to the objects found
# in the original -> Faz uma copia do original
original_list = [1, 2, 3]
copied_list = original_list.copy()
original_list.append(4)
print(original_list, copied_list)

# Deep copy
# Creates a new object and recursively copies all objects found in the original.
nested_list = [[1, 2, 3], [4, 5, 6]]
deep_copied_list = copy.deepcopy(nested_list)
nested_list[0].append(7)
print(nested_list, deep_copied_list)

#-----------------------------------------------------------------------
# Example
# This unpredictable behavior is because the shallow copy only creates a 
# new reference for the top-level object, but nested mutable objects are 
# still referenced by both the original and the copy.
list_of_numbers = [[1, 2, 3], [4, 5, 6]]
# Creating a shallow copy
shallow_copy = copy.copy(list_of_numbers)
# Making changes to the shallow_copy
shallow_copy[0][0] = 0

print(f"Original List: {list_of_numbers}")
print(f"Shallow copy: {shallow_copy}")

# Instead of a shallow copy, create a deep copy. A deep copy breaks all 
# references to the original and creates a new object. This means 
# that changes made to the nested objects in the original or copied 
# object will not affect each other
deep_copy = copy.deepcopy(list_of_numbers)
deep_copy[0][0] = 0
print(f"Original List: {list_of_numbers}")
print(f"Deep copy: {deep_copy}")

# Now that we have created a deep copy, the changes that we have made to 
# the deep copy have no effect on the original list.

#-----------------------------------------------------------------------
# Avoid unintended Side effects with default arguments
# The issue here voce esta chamando a funcao e esperava que toda vez
# fosse criado uma lista vazia. So que a lista esta sendo preenchida.
def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list

# Call funtion first time
result_1 = append_to_list(1)
print(f"Results 1: {result_1}")

# Call function second time
result_2 = append_to_list(2)
print(f"Results 2: {result_2}")

# Call function third time
result_3 = append_to_list(3)
print(f"Results 2: {result_3}")

# Para evitar esse comportamento, vamos passar um IMMUTABLE object as default
# argument.And initialize the empty list inside the function.
def append_to_list(value, my_list=None):
    if my_list == None:
        my_list = []
    my_list.append(value)
    return my_list

# With this modification, each call to append_to_list starts with a new empty 
# list. The unexpected accumulation of elements has been eliminated.
# When we call the function, we start with an empty list.