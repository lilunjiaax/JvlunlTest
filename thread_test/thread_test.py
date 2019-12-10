

import time
import threading
import queue

from thread1 import before_test


q = queue.Queue()
for i in range(6):
    start_time = time.time()
    try:
        threadA = threading.Thread(target=before_test, args=('llj', 12, q))
        threadA.start()
        threadA.join()
    except:
        pass
    if not q.empty():
        print(q.get())
    print("主xian程 执行 {}".format(i))
    end_time = time.time()
    time.sleep(2)
    print(start_time, end_time)





