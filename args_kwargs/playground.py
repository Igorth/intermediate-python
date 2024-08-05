if __name__ == "__main__":
    # Default parameters
    # Can make your functions more flexible and user-friendly. 
    # They are especially useful when you have a function with many parameters 
    # and most of them could have sensible defaults
    def create_user(username, is_active=True, role="member"):
        print(f"Username: {username}")
        print(f"Active: {'Yes' if is_active else 'No'}")
        print(f"Role: {role}")

    # Create a new active user with a role of 'member' by default
    create_user("john")
    create_user("lai", is_active=False, role="admin")

# Things to Remember with Default Parameters
# Default parameters should be defined after non-default parameters 
# in a function definition.
# Changing mutable defaults (like lists or dictionaries) can lead to 
# unexpected behavior. It's usually safer to use None as the default and 
# add a check inside the function.
# Default parameter values are evaluated only once, at the time the function 
# is defined, not each time the function is called.

#------------------------------------------------------------------------------
# *args
# Consider a real-world scenario where you want to log several 
# messages with a single function call
def log_messages(*messages):
    for message in messages:
        print(f"LOG: {message}")

#log_messages("Server started", "Database connected")

#------------------------------------------------------------------------------
def concatenate_strings(*args):
    result = ""
    for item in args:
        result += item
    return result
greetings = concatenate_strings("hi ", "how")
#print(greetings)

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# **kwargs
# **kwargs is a Python convention that allows you to pass a variable number of 
# keyword arguments to a function. The term kwargs stands for "keyword 
# arguments," and the double asterisk ** is a syntax that unpacks a dictionary 
# of key-value pairs into the function's arguments. This means that within the 
# function, kwargs becomes a dictionary holding all the keyword arguments 
# that were passed.
def calculate(n, **kwargs):
    print(kwargs)  # Type DICT
    for key, value in kwargs.items():
        print(key, value)
    
    n += kwargs["add"]
    print(n)
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def configure(**kwargs):
    config = {
        'output_format': 'json',
        'verbose': False
    }
    config.update(**kwargs)  # Update the default config with any user-specified kwargs.
    return config

user_config = configure(output_format="xml", retries=3)
print(user_config)
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# When you call user_profile(name="Alice", age=30, city="Wonderland"), each named argument is packed into a dictionary by **kwargs.
# Inside the function, kwargs is a dictionary with keys and values corresponding to the argument names and their values: {'name': 'Alice', 'age': 30, 'city': 'Wonderland'}.
# You can then iterate over the kwargs dictionary and print out the user profile information.
def user_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

user_profile(name="Igor", age=3, city="Wonder")
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
def html_tag(tag, **attributes):
    attr_str = ' '.join(f'{key}="{value}"' for key, value in attributes.items())
    return f"<{tag} {attr_str}></{tag}"

print(html_tag("a", href='http://example.com', title="Example"))
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="nissa")
print(my_car.model)
print(my_car.make)