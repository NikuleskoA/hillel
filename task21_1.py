import pytest

class Manager:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        if not isinstance(name, str) or not isinstance(age, int) or not isinstance(salary, (int, float)):
            raise ValueError

    def __str__(self):
        return f"{self.__class__.__name__}; dict={self.__dict__}"

    def get_year_salary(self):
        return self.salary*12

    def get_real_salary(self):
        return self.salary*0.9

    def salary_increase(self, a):
        if not isinstance(a, (int, float)):
            raise ValueError
        if a < 0:
            raise ValueError
        self.salary = self.salary + a


def test_get_year_salary():
    m = Manager("John", 20, 1000)
    assert m.get_year_salary() == 12000

def test_get_real_salary():
    m = Manager("John", 20, 1000)
    assert m.get_real_salary() == m.salary*0.9

def test_construct():
    with pytest.raises(ValueError):
        Manager("John", "dnaif", 1000)

    with pytest.raises(ValueError):
        Manager(1222, 20, 1000)

    with pytest.raises(ValueError):
        Manager(1222, 20, "fqeefweqf")

def test_salary_increase():
    m = Manager("John", 20, 1000)
    m.salary_increase(1000)
    assert m.salary == 2000

def test_salary_increase_error():
    with pytest.raises(ValueError):
        m = Manager("John", 20, 1000)
        m.salary_increase("x20")
