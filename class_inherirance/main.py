class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.num_eyes = 5

    def breathe(self):
        super().breathe()
        print("doing this underwater")

    def swim(self):
        print("moving in the water")


nemo = Fish()
print(nemo.num_eyes)