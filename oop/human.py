class Human:
    MAX_ENERGY = 100

    def __init__(self, name="Human", age=0):
        self.name = name
        self.age = age
        self.energy = Human.MAX_ENERGY

    # instance methods
    def display(self):
        print(f"I am {self.name}")

    # magic methods
    def __repr__(self):
        return f'human(name={self.name}, age={self.age}, energy={self.energy})'

    def __str__(self):
        return f'My name is {self.name} and I am {self.age} years old and my energy is {self.energy}.'


if (__name__ == "__main__"):
    human = Human()
    human.display()
    print(repr(human))
    print(str(human))

