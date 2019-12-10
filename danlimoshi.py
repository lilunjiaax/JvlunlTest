class Single(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(Single, cls).__new__(cls)
        return cls._instance 
    def __init__(self, name, age):
        self.name = name
        self.age = age

a = Single('kkp', 18)
# print(a.name)
b = Single("haha", 19)
# print(b.name)  # haha
# print(a.name)  # haha
# print(id(a),id(b))  # 2615182656512 2615182656512

class A:
    def __init__(self):
        self.name = "zhangp"
        
    def method(self):
        print("method print")
        
a = A()

print(getattr(a, 'name', "no name"))
print(getattr(a, 'age', "no age"))

print(getattr(a, 'method', 'no methos'))

setattr(a, 'name1', 'cat')

print(a.name1)












