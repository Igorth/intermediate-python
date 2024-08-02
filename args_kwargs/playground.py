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

log_messages("Server started", "Database connected")

#------------------------------------------------------------------------------
def concatenate_strings(*args):
    result = ""
    for item in args:
        result += item
    return result
greetings = concatenate_strings("hi ", "how")
print(greetings)

#------------------------------------------------------------------------------
