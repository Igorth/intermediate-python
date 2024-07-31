x = [i for i in range(10)]
#print(x)

z = []
for i in range(10):
    z.append(i)
#print(z)

a = [[j for j in range(10)] for i in range(10)]
#print(a)

b = [i for i in range(10) if i % 2 == 0]
#print(b)

#----------------------------------------------------------------------
# Example Map and List Comprehension
def square(x):
    return x * x

numbers = [4, 2, 1, 6, 9, 7]
using_map = list(map(square, numbers))
print(using_map)

using_list_comp = [square(x) for x in numbers]
print(using_list_comp)

#----------------------------------------------------------------------
# Example Filter and List Comprehension
def is_odd(x):
    return bool(x % 2)

using_filter = list(filter(is_odd, numbers))
print(using_filter)

using_list_compre = [x for x in numbers if is_odd(x)]
print(using_list_compre)