import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Start time
        result = func(*args, **kwargs)  # Call the decorated function
        end_time = time.time()  # End time
        print(f"Function {func.__name__} took: {end_time - start_time:.4f} sec.")
        return result
    return wrapper

@timer
def example_function(n):
    return f"The sum is {sum(range(n))}"

print(example_function(100000000))