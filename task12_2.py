class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def L(self, other):
        l = pow(((self.x-other.x)**2+(self.y-other.y)**2), 1/2)
        return l
    def S(self, other):
        s = (self.y+other.y)*abs(self.x-other.x)/2
        return s

class Polygon:
    def __init__(self, args:list):
        self.points = args
    def P(self):
        l = len(self.points)
        list1 = self.points
        list1.append(self.points[0])
        p = 0
        for i in range(l):
            p = p + Point.L(list1[i], list1[i+1])
        return p
    def S(self):
        l = len(self.points)
        list1 = self.points
        list1.append(self.points[0])
        s = 0
        for i in range(l):
            s = s + (list1[i].x*list1[i+1].y - list1[i+1].x*list1[i].y)
        return abs(s/2)


p1=Point(0, 0)
p2=Point(0, 4)
p3=Point(3, 0)
print("Длина отрезка: ",Point.L(p1, p2))
print("Площадь под отрезком: ",Point.S(p2, p3))
pol = Polygon([p1, p2, p3])
print("Периметр: ",pol.P())
print("Площадь: ",pol.S())
pol = Polygon([Point(1, 1), Point(3, 5), Point(8, 5), Point(10, 1)])
print("Площадь: ",pol.S())
