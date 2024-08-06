# Functions can have inputs/functionality/output

if __name__ == "__main__":
    # def add(n1, n2):
    #     return n1 + n2
    #
    #
    # def subtract(n1, n2):
    #     return n1 - n2
    #
    #
    # def multiply(n1, n2):
    #     return n1 * n2
    #
    #
    # def divide(n1, n2):
    #     return n1 / n2
    #
    #
    # # First-class objects, can be passed around as arguments e.g int/str/float
    #
    #
    # def calculate(calc_function, n1, n2):
    #     return calc_function(n1, n2)
    #
    #
    # # Testing the functions
    # result = calculate(add, 5, 3)
    # print("Addition: ", result)
    #
    # # Nested functions
    #
    #
    # def outer_function():
    #     print("I'm outer")
    #
    #     def nested_function():
    #         print("I'm nested")
    #
    #     nested_function()
    #
    # outer_function()

    # # Functions can be returned from other functions
    # def outer_function():
    #     print("I'm outer")

    #     def nested_function():
    #         print("I'm nested")

    #     return nested_function

    # inner_function = outer_function()
    # inner_function()

#------------------------------------------------------------------------------
    # Python Decorator Function
    # A decorator function is simply a function which wraps another function and gives
    # it some additional functionality or modifies the functionality
    import time

    def delay_decorator(function):
        def wrapper_function():
            time.sleep(2)  # Simulating some heavy computation
            # Do something before calling the original function
            # Antes de rodar a funcao original say_hello() eu executo o time.sleep(2)
            function()
            function()
        return wrapper_function

    @delay_decorator  # @ sign is the syntactic sugar
    def say_hello():
        print("Hello!")

    def say_goodbye():
        print("Goodbye!")

    def say_greetings():
        print("Greetings!")

    say_hello()