class GoodOrder:
    def __init__(self):
        self.str1 = input("Введите последовательность скобок: ")

    def is_ordered(self, brackets="{}[]()<>"):
        o, cl = brackets[::2], brackets[1::2]
        list1 = []
        for i in self.str1:
            if i in o:
                list1.append(o.index(i))
            elif i in cl:
                if list1 and list1[-1] == cl.index(i):
                    list1.pop()
                else:
                    return "Не является правильной скобочной последовательностью"
        return "Правильная скобочная последовательность"

p=GoodOrder()
print(p.is_ordered())
