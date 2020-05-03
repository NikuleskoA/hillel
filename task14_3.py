import time

class MyContext():
    def __init__(self):
        self.t = None
        self.f_t =None

    def __enter__(self):
        self.t = time.time()

    def __exit__(self, *args):
        self.f_t = time.time()-self.t
        print("Time: ", self.f_t)

    def __call__(self, func):
        self.func = func
        def wrapper(*args):
            t= time.time()
            res = func(*args)
            print("{0}() была выполнена за: {1}".format(func.__name__, time.time()-t))
            return res
        return wrapper

@MyContext()
def foo():
    a = 1
    b = 0
    for i in range(1_000_000):
        if b != 0:
            c = a/b

@MyContext()
def foo1():
    for i in range(1_000_000):
        try:
            a = 1/0
        except ZeroDivisionError:
            pass
foo()
foo1()


with MyContext():
    a = 1
    b = 0
    for i in range(1_000_000):
        if b != 0:
            c = a/b

with MyContext():
    for i in range(1_000_000):
        try:
            a = 1/0
        except ZeroDivisionError:
            pass
