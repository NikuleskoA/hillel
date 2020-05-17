import datetime
import itertools
import string
from asyncio import Queue
from zipfile import ZipFile

import asyncio

THREAD_NUMBER = 5
found = False

async def worker(q: Queue, num):
    print(f"Started worker {num}")
    global found
    with ZipFile(r"lesson6.zip", "r") as f:
        while not found:
            password = await q.get()
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

async def generator(q: Queue):
    print(f"Started generator")

    global found
    gen = itertools.product(string.ascii_lowercase, repeat=3)  # генератор сочетаний с повторениями из 3х букв
    max_queue_size = 10
    for combination in gen:
        if found:
            break
        while q.qsize() > max_queue_size:
            await asyncio.sleep(0)
        combination = "".join(combination)
        combination = combination.encode('utf8')
        print(combination)
        await q.put(combination)
        print(q)

    for i in range(THREAD_NUMBER):
        await q.put(None)
    print(f"Finished generator")


if __name__ == '__main__':

    start = datetime.datetime.now()

    q = Queue()

    loop = asyncio.get_event_loop()

    tasks = asyncio.gather(generator(q), *[worker(q, i) for i in range(THREAD_NUMBER)])
    print(tasks)
    loop.run_until_complete(tasks)
    finish = datetime.datetime.now() - start
    print(finish)