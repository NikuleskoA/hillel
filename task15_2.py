class Person:
    def __init__(self, name):
        self.name = name

def foo1(self):
    print('manager ' + self.name)

Manager = type('Manager', (Person,), {'func1': foo1})
manager = Manager('John')
manager.func1()