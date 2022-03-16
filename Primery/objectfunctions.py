class Parentclass:
    def __init__(self):
        self.a = 1
        print("Parent Class Object Created")

    def someMethod(self):
        print("hello")


class ChildClass(Parentclass):
    def __init__(self):
        print("Child Class Object Created")

parent = Parentclass()
child = ChildClass()