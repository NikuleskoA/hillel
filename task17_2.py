class ReverseIterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = len(collection)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= 0:
            raise StopIteration
        self.index = self.index - 1
        return self.collection[self.index]

list1 = (3, 2, 1, 'two', 'one', [1, '1'])
r_list = ReverseIterator(list1)
print(list(r_list))

for i in ReverseIterator(list1):
    print(i)


