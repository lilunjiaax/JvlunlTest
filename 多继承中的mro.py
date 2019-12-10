# super继承:MRO(方法解析顺序method resolution order)
class A:
    def __init__(self):
        print("enter A")
        print("leave A")

class B(A):
    def __init__(self):
        print("enter B")
        super(B, self).__init__()
        print("leave B")

class C(A):
    def __init__(self):
        print("enter C")
        super(C, self).__init__()
        print("leave C")

class D(A):
    def __init__(self):
        print("enter D")
        super(D, self).__init__()
        print("leave D")

class E(B, C, D):
    def __init__(self):
        print("enter E")
        super(E, self).__init__()
        print("leave E")

# 多重继承的拓扑排序为：E , B ,C , D , A
# 对于多重继承，如何决定他的MRO顺序呢：使用C3算法：对于此无向图进行拓扑排序
E()
print(E.mro())


