import functools

def singleton(class1):
    instances = {}
    @functools.wraps(class1)
    def wrapper(*args, **kwargs):
        if class1 not in instances:
            instances[class1] = class1(*args, **kwargs)
            return instances[class1]
        return wrapper

@singleton
class DBConnection:
    def __init__(self):
        pass
    def __str__(self):
        return 'Database connection object'
c1 = DBConnection
c2 = DBConnection
print("id(c1): {}".format(str(id(c1))))
print("id(c2): {}".format(str(id(c1))))
print(c1 is c2)