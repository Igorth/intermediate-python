def func(x, y):
    x = x - 1  # The 1 was copy over to the function and stored in X
    y.pop()

if __name__ == "__main__":
    i = 1 # pass by value
    l = ['a', 'b'] # pass by reference

    func(i, l)
    print(i, l)