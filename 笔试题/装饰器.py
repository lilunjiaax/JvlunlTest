"""
装饰器：
"""
import time

# 不带参数的函数装饰器
# def decorate(func):
#     def wrapper():
#         before = time.time()
#         print("不带参数的装饰器执行")
#         info = func()
#         after = time.time()
#         print("函数执行时间：%s" % str(after - before))
#         return info
#     return wrapper


# @decorate
# def test():
#     return '函数执行'

# print(test())


# 带参数的装饰器
# 主要注意接收参数，接收函数对象

# def calcute_time(limit):
#     def wrapper(func):
#         def foo(*args, **kwargs):
#             before = time.time()
#             print("不带参数的装饰器执行")
#             info = ''
#             for i in range(limit):
#                 print("第{}次执行".format(i+1))
#                 info += func(*args, **kwargs)
#             after = time.time()
#             print("函数执行时间：%s" % str(after - before))
#             return info
#         return foo
#     return wrapper

# @calcute_time(6)
# def add_str(a_str, num):
#     return a_str*num


# print(add_str('llj', 2))

#### 下面探讨一下关于类装饰器（类装饰器如何传递参数，被装饰对象如何传递参数）

# 不带参数（装饰器不带，函数不带）
# 当都不携带参数时，类装饰器直接将函数传给 实例属性
# class Timer:
#     def __init__(self, func):
#         self._func = func
    
#     def __call__(self, *args, **kwargs):
#         before = time.time()
#         self._func()
#         after = time.time()
#         print("函数执行时间：%s" % str(after - before))


# @Timer
# def foo():
#     print("被类装饰的函数执行")

# foo()


# 函数携带参数，类装饰器不携带参数
# 注意函数的执行和返回对象
# class Timer:
#     def __init__(self, func):
#         self._func = func
    
#     def __call__(self, *args, **kwargs):
#         before = time.time()
#         self._func(*args, **kwargs)
#         after = time.time()
#         print("函数执行时间：%s" % str(after - before))
#         return self._func(*args, **kwargs)


# @Timer
# def foo(a, b):
#     print(f"被类装饰的函数执行 : {a+b}" )

# foo('aaa', 'bbb')



# 函数不携带携带参数，类装饰器携带参数
# 一种调用处理办法
# class Timer:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __call__(self, func, *args, **kwargs):
#         before = time.time()
#         print(f"类传递进来的参数和：{self.x+self.y}")
#         print(f"被装饰函数的名字：{func.__name__}")
        
#         after = time.time()
#         print("函数执行时间：%s" % str(after - before))
#         return func


# @Timer(1,2)
# def foo():
#     print(f"被类装饰的函数执行")

# foo()

# 另一种执行调用方法，但显然第一种更好
# 因为这一种会导致装饰即调用
# class Timer:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __call__(self, func, *args, **kwargs):
#         before = time.time()
#         print(f"类传递进来的参数和：{self.x+self.y}")
#         print(f"被装饰函数的名字：{func.__name__}")
#         func()
#         after = time.time()
#         print("函数执行时间：%s" % str(after - before))


# @Timer(1,2)
# def foo():
#     print(f"被类装饰的函数执行")

# 类装饰器，函数都携带参数
class Timer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __call__(self, func, *args, **kwargs):
        before = time.time()
        print(f"类传递进来的参数和：{self.x+self.y}")
        print(f"被装饰函数的名字：{func.__name__}")
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            print("Ending!!")
        after = time.time()
        print("函数执行时间：%s" % str(after - before))
        return wrapper
        


@Timer(1,2)
def foo(x, y):
    print(f"被类装饰的函数执行:{x, y}")

foo(1, 2)





