# Lists: ordered, mutable, allows duplicate elements => []
# Tuple: ordered, immutable, allows duplicate elements -> ()
# Dictonary: key-values pairs, unordered, mutable -> {}
# Sets: unordered, mutable, no duplicates -> {}

# Immutable -> once you define you can not change (str, int, float, bool, bytes, tuple)
# Mutable -> can change (list, set, dict)

#------------------------------------------------------------------------
# Using as Tuple IMMUTABLE
x = (1, 2)
y = x # Whenever you are using immutable types, when you do an assigmnent
      # to another variable, it makes a COPY.

x = (1, 2, 3)
#print(x, y)

#------------------------------------------------------------------------
# Using as List MUTABLE
# When you are using mutable types, you are assing a variable to another
# variable an this variable storing a MUTABLE type. 
# What happens is you actually store a REFERENCE or an alias to this same object
a = [1, 2]
b = a

a[0] = 100
#print(a, b)

#------------------------------------------------------------------------
# Example
# When we call this function we pass the nums LIST as the parameter numbers.
# Since we are passing a MUTABLE object, a list is MUTABLE
# When we do an numbers.sort() is sort the list in place
# The numbers in the function is going to be storing a REFERENCE to the
# same list
def get_largest_numbers(numbers, n):
    numbers.sort()

    return numbers[-n:]

nums = [2, 3, 4, 1, 34, 123, 321, 1]
print(nums)
largest = get_largest_numbers(nums, 2)
print(nums)

#------------------------------------------------------------------------
# Immutable
# When you change the value of an immutable object, a new object is created,
# and the reference is updated to point to this new object.
a = 10
b = a
print(a, b)  # Output: 10 10

a = 20
print(a, b)  # Output: 20 10

#------------------------------------------------------------------------
# Mutable
# Here, list1 and list2 refer to the same list object. Modifying the list
# through list1 also affects list2 because both references point to the 
# same object.
list_1 = [1, 2, 3]
list_2 = list_1
print(list_1, list_2)

list_1.append(4)
print(list_1, list_2)

#------------------------------------------------------------------------
