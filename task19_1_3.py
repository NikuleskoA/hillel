import datetime
import multiprocessing as mp
import time
from multiprocessing import Queue
PROCESSORS = 2
#Реализация через процессы
def is_prime(num):
    if num <= 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5 + 1)):
        if num % i == 0:
            return False
    return True

def worker(q: Queue, wid):
    print(f'worker {wid} started')
    while True:
        num = q.get()
        if num is None:
            break
        if is_prime(num):
            print(wid, num)
    print(f'worker {wid} stopped')

def generator(q: Queue):
    print('generator start')
    max_queue_size = 50
    for it in range(1, 1_000_000):
        while q.qsize() >= max_queue_size:
            time.sleep(0.000001)
        q.put(it)
    for i in range(PROCESSORS):
        q.put(None)
    print('generator exit')

if __name__ == '__main__':
    start = datetime.datetime.now()
    q = Queue()
    pr = mp.Process(target=generator, args=(q,))

    workers = []
    for i in range(PROCESSORS):
        w = mp.Process(target=worker, args=(q, i))
        w.start()
        workers.append(w)

    pr.start()
    pr.join()

    for i in range(PROCESSORS):
        workers[i].join()

    finish = datetime.datetime.now()
    print(f'finish: {finish - start}')