from contextlib import contextmanager
import time

@contextmanager
def foo():
    t = time.time()
    try:
        yield
    except Exception:
        pass
    print("Время выполнения блока: ", time.time()-t)

with foo() as f:
    time.sleep(1)
    raise Exception()
