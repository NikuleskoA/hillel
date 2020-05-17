import threading
import time

import requests
import queue

from urllib3.exceptions import ConnectTimeoutError

MAX_THREAD_NUM = 250
MAX_Q_SIZE = 100

url = "http://httpbin.org/ip"

def worker(q: queue.Queue):
    while True:
        pr = q.get()
        if pr is None:
            break
        try:
            r = requests.Session().get(url, timeout=0.5, proxies=pr)
            print(f"{r.status_code}\n", end="")
            print(f"{pr}\n", end="")

        except (ConnectTimeoutError,
                requests.exceptions.ConnectTimeout,
                requests.exceptions.ProxyError,
                requests.exceptions.ReadTimeout,
                requests.exceptions.TooManyRedirects,
                requests.exceptions.ConnectionError,
                requests.exceptions.ChunkedEncodingError) as e:
            print(f"{e}\n", end="")


def generator(q: queue.Queue):
    with open("p_file.txt") as proxies:
        for p in proxies:
            while q.qsize() > MAX_Q_SIZE:
                time.sleep(0.000001)
            pr = p.strip()
            q.put({'http': f'http://{pr}'})
    for _ in range(MAX_THREAD_NUM):
        q.put(None)

if __name__ == '__main__':
    q = queue.Queue()
    gen_thread = threading.Thread(target=generator, args=(q,))
    gen_thread.start()
    workers = []
    for i in range(MAX_THREAD_NUM):
        w = threading.Thread(target=worker, args=(q,))
        w.start()
        workers.append(w)
    gen_thread.join()
    [i.join() for i in workers]