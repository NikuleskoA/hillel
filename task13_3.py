import time

class ContManager:
    def __enter__(self):
        self.start = time.time()
        
    def __exit__(self, type, value, traceback):
        print("Время выполнения  " + str(time.time()-self.start))

with ContManager():
    for i in range(1_000_000):
        pass