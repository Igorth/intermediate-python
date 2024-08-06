def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}")
        result = function(*args)
        print(f"It returned {result}.")
    return wrapper


@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)

#---------------------------------------------------------------------------
# Advanced Python Decorator Functions

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
        else:
            print("You must be logged in to access this page.")
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("John Doe")
new_user.is_logged_in = True
create_blog_post(new_user)
