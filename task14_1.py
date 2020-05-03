class MyException(Exception):
    def write_to_file(self):
        with open('text1.txt', 'a') as f:
            f.write("Something wrong\n")


try:
    raise MyException
except MyException as me:
    me.write_to_file()