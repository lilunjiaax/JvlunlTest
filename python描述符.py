class Desc(object):
    
    def __get__(self, instance, owner):
        print("__get__...")
        print("self : \t\t", self)
        print("instance : \t", instance)
        print(id(instance))
        print("owner : \t", owner)
        print(id(owner))
        print('='*40, "\n")
        
    def __set__(self, instance, value):
        print('__set__...')
        print("self : \t\t", self)
        print("instance : \t", instance)
        print("value : \t", value)
        print('='*40, "\n")


class TestDesc(object):
    x = Desc()

#以下为测试代码
t = TestDesc()
t.x

print(id(t))
print(id(TestDesc))
