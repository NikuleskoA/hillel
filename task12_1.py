class Figure:
    def P(self):
        raise Exception
    def S(self):
        raise Exception
class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def P(self):
        return  self.a+self.b+self.c
    def S(self):
        p = self.P()/2
        s=pow(p*(p-self.a)*(p-self.b)*(p-self.c), 1/2)
        return s
class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def P(self):
        return (self.a + self.b)*2
    def S(self):
        return self.a * self.b

class Circle(Figure):
    def __init__(self, a):
        self.a = a
    def P(self):
        p = self.a*2*3.14
        return p
    def S(self):
        s = 3.14*self.a**2
        return s

t = Triangle(3, 4, 5)
print(t.P())
print(t.S())
r = Rectangle(3, 5)
print(r.P())
print(r.S())
c = Circle(3)
print(c.P())
print(c.S())

