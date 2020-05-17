import datetime
import threading
import time
from queue import Queue
THREAD_NUMBER = 4
#Реализация через потоки
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
    for i in range(1, 1_000_000):
        while q.qsize() >= max_queue_size:
            time.sleep(0.000001)
            # pass
        q.put(i)
    for i in range(THREAD_NUMBER):
        q.put(None)
    print('generator exit')

start = datetime.datetime.now()

q = Queue()
gthread = threading.Thread(target=generator, args=(q,))
gthread.daemon = True

workers = []
for i in range(THREAD_NUMBER):
    w = threading.Thread(target=worker, args=(q, i))
    w.daemon = True
    w.start()
    workers.append(w)

gthread.start()
gthread.join()

for i in range(THREAD_NUMBER):
    workers[i].join()

finish = datetime.datetime.now()
print(f'finish: {finish - start}')