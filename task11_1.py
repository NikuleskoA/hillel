class Person:
    def __init__(self, age, name, prof, salary):
        self.p_age = age
        self.p_name = name
        self.p_prof = prof
        self.p_salary = salary
    def __str__(self):
        return f'{self.__class__.__name__}({self.__dict__})'

class Manager(Person):
    def __init__(self, age=25, name="Bill", prof="manager", salary=2500, experience=3):
        super().__init__(age, name, prof, salary)
        self.m_experience = experience


p = Person(58, "Alex", "postmaster", 2000)
print(p)
m = Manager()
print(m)
m1 = Manager(34, "John", salary=2000)
print(m1)

