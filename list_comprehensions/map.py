#---------------------------------------------------
# Syntax
# map(function, iterables)


# Example 1 Using Map
strings = ["my", "world", "orange", "apple"]
lengths = map(len, strings)
print(lengths)
print(list(lengths))

#---------------------------------------------------
# Example 2 Using List Comprehension
a = [len(i) for i in strings]
print(a)

#---------------------------------------------------
# Example 2 Using Map
def my_func(n):
    return len(n)

x = map(my_func, ('apple', 'banana', 'pera'))
print(list(x))

#---------------------------------------------------
# Example 2 Using List Comprehension
b = [my_func(i) for i in ('apple', 'banana', 'pera')]
print(b)