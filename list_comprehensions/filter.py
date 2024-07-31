# Filter
#---------------------------------------------------
# Example 1 Using Filter
ages = [5, 12, 17, 18, 24, 32]

def calc_age(x):
    if x < 18:
        return False
    else:
        return True
    
adults = filter(calc_age, ages)
print(adults)
print(list(adults))

#---------------------------------------------------
# Example 1 Using List Comprehension
adults_two = [x for x in ages if calc_age(x)]
print(adults_two)

#---------------------------------------------------
# Example 2 Using Filter
def longer_than_4(string):
    return len(string) > 4

strings = ["my", "world", "orange", "apple"]
filtered = filter(longer_than_4, strings)
print(filtered)
print(list(filtered))

#---------------------------------------------------
# Example 2 Using List Comprehension
filter_words = [x for x in strings if longer_than_4(x)]
print(filter_words)