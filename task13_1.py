def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except:
            return None
        return result
    return wrapper

@exception_handler
def func(a):
    print(1/a)

func(0)
func(1)


class Exception_Cont_M:
    def __enter__(self):
        pass
    def __exit__(self, type, value, traceback):
        return True

def func1(a):
    print(1/a)

with Exception_Cont_M():
    func1(0)

with Exception_Cont_M():
    func1(1)