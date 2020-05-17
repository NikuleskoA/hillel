import datetime
import itertools
import string
import threading
import time
from queue import Queue
from zipfile import ZipFile

THREAD_NUMBER = 4
found = False

def worker(q: Queue, num):
    print(f"Started worker {num}")
    global found
    with ZipFile(r"lesson6.zip", "r") as f:
        while not found:

            password = q.get()
            if password is None:
                break
            print(f"{password}\n", end="")
            try:
                f.extract(r"lesson6/file_16.txt", "directory", pwd=password)
                found = True
                print("ok")
                break
            except Exception as e:
                print(e)
    print(f"Finished worker {num}")

def generator(q: Queue):
    print(f"Started generator")

    global found
    gen = itertools.product(string.ascii_lowercase, repeat=3)
    max_queue_size = 10
    for combination in gen:
        if found:
            break
        while q.qsize() > max_queue_size:
            time.sleep(0.0000001)
        combination = "".join(combination)
        combination = combination.encode('utf8')
        q.put(combination)

    for i in range(THREAD_NUMBER):
        q.put(None)
    print(f"Finished generator")

if __name__ == '__main__':
    start = datetime.datetime.now()

    q = Queue()
    thread_g = threading.Thread(target=generator, args=(q,))
    workers = []
    for i in range(THREAD_NUMBER):
        w = threading.Thread(target=worker, args=(q, i))
        w.start()
        workers.append(w)

    thread_g.start()
    thread_g.join()

    for w in workers:
        w.join()

    finish = datetime.datetime.now() - start
    print(finish)