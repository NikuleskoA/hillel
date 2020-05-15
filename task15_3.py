class EmailDescriptor:
    def __get__(self, instance, owner):
        return instance._email
    def __set__(self, instance, value: str):
        if '@' in value:
            str1 = value.split("@")
            if len(str1[0])>0 and len(str1[1])>0:
                instance._email = value
                print('Новое значение ', value)
            else:
                raise Exception('Неправильный email')
        else:
            raise Exception('Неправильный email')

class Email:
    def __init__(self, email):
        self.email = email
    email = EmailDescriptor()

email = Email("my_email@gmail.com")
email.email = "new_email@gmail.com"
email.email = "aaa@"