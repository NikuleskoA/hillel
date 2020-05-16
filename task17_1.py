class MyRange:
    def __init__(self, *args):
        args_tuple = tuple(args)
        self.start = 0
        self.step = 1
        if len(args_tuple) == 1:
            self.stop = args_tuple[0]
        elif len(args_tuple) == 2:
            self.start, self.stop = args_tuple
        elif len(args_tuple) == 3:
            self.start, self.stop, self.step = args_tuple

    def __iter__(self):
        return self

    def __next__(self):
        if self.step == 0:
            raise StopIteration
        elif self.start<=self.stop and self.step<0 or self.start>=self.stop and self.step>0:
            raise StopIteration
        self.start += self.step
        return self.start - self.step

print("MyRange():")
for i in MyRange(10):
    print(i, end=' ')
print()
for i in MyRange(5, 15):
    print(i, end=' ')
print()
for i in MyRange(5, 25, 2):
    print(i, end=' ')
print()

def my_generator(*args):
    args_tuple = tuple(args)
    start = 0
    step = 1
    if len(args_tuple) == 1:
        stop = args_tuple[0]
    elif len(args_tuple) == 2:
        start, stop = args_tuple
    else:
        start, stop, step = args_tuple
    while start > stop and step < 0 or start < stop and step > 0 and step!=0:
        yield start
        start += step

print("my_generator():")
for i in my_generator(10):
    print(i, end=' ')
print()
for i in my_generator(5, 15):
    print(i, end=' ')
print()
for i in my_generator(5, 25, 2):
    print(i, end=' ')
print()