# Removing duplicates from a list while applying a function
nums = [1, 2, 3, 4, 5, 4, 4, 4, 3, 3,3, 3, 2, 2]

unique_squares = {x**2 for x in nums}
print(unique_squares)