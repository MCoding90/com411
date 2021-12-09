class Robot:
    MAX_ENERGY = 100

    def __init__(self, name="Robot", age=0):
        self.name = name
        self.age = age
        self.energy = Robot.MAX_ENERGY

    # instance methods
    def display(self):
        print(f"I am {self.name}")

    # magic methods
    def __repr__(self):
        return f'robot(name={self.name}, age={self.age}, energy={self.energy})'

    def __str__(self):
        return f'My name is {self.name} and I am {self.age} years old and my energy is {self.energy}.'


if (__name__ == "__main__"):
    robot = Robot()
    robot.display()
    print(repr(robot))
    print(str(robot))
