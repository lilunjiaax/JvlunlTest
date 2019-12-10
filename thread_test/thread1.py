import time
import os


def before_test(user_name, age, q):
    q.put(12)
    for i in range(10):
        time.sleep(2)
        print("用户:{} ,年龄: {} ,  模块名：{}".format(user_name, age, __name__))
        if i == 6:
            assert False

















