def decorator_maker(*args):
    err_tuple = args
    def exc_handler(func):
        def wrapper(*args):
            try:
                result = func(*args)
            except err_tuple:
                return print("Возникла ошибка но была подавлена")
            return result
        return wrapper
    return exc_handler


@decorator_maker(ZeroDivisionError, NameError, TypeError)
def func(a):
    if a == 1:
        print(1/0)
    if a == 2:
        print(spam*2)
    else:
        print('2' + 2)

func(1)
func(2)
func()
