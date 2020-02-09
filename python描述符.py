class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._register = {
            'name': name,
            'age': age
        }

    def __getitem__(self, item):
        # if item in self._register:
        #     return self._register[item]
        # return None
        return self._register.get(item, None)

    def __setitem__(self, key, value):
        self._register[key] = value

    def __getattr__(self, item):
        """
        1. 调用实例对象的某些属性/方法不存在时会执行该函数：user.aa / user.func1()，
	    2. 想要实现反射时，可以使用setattr(),getattr()方法
        :param item:
        :return:
        """
        print("不存在:{}".format(item))
        return

    def __del__(self):
        """
        当程序执行完毕时，该对象被回收内存销毁了，执行该函数
        :return:
        """
        print("对象被销毁")

    def __len__(self):
        return len(self._register)

    def __call__(self, *args, **kwargs):
        """
        此方法能够使实例对象如同函数一样被调用
        实现斐波那契数列
        :param args:
        :param kwargs:
        :return:
        """
        assert len(args) == 1
        _a = 0
        _b = 1
        _end = args[0]
        _a_list = []
        while _a < _end:
            _a_list.append(_a)
            _a, _b = _b, _a + _b

        return _a_list, sum(_a_list)

# user = User('aa', 16)
# print(user['name'])
# user['gender'] = 'kk'
# print(user(22))
# print(len(user))


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


# class TestDesc(object):
#     x = Desc()

# #以下为测试代码
# t = TestDesc()
# t.x

# print(id(t))
# print(id(TestDesc))
