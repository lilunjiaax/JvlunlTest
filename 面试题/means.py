import pickle
from pandas import DataFrame


class Read(object):
    """
    获取传送过来的文件名（默认在同一目录）
    """
    def __init__(self, name):
        self.name = name

    def read(self):
        print('你需要打开的文件为：%s' % self.name)
        with open(self.name, 'rb') as file:
            root = pickle.load(file)
        id_frm = root['id_frm']
        feature_frm = root['feature_frm']

        # 获取id关系的DataFrame
        # index:div_id  cols:id_page
        div = id_frm['div']
        # index:div_cc_id  cols:id_div
        div_cc = id_frm['div_cc']
        # index:div_tt_id   cols:id_div
        div_tt = id_frm['div_tt']
        # index:div_c_t_id  cols:div_cc_id
        div_c_t = id_frm['div_c_t']

        # 获取位置以及内容
        # index:div_id   cols:x_value,y_value
        div2 = feature_frm['div']
        # index:div_cc_id  cols:height,weight
        div_cc2 = feature_frm['div_cc']
        # index:div_c_t_id   cols:x_value,y_value,string
        div_c_t2 = feature_frm['div_c_t']
        div_list = [div, div_cc, div_tt, div_c_t, div2, div_cc2, div_c_t2]
        # 在类的实例化时可以直接解包，将列表里面的值直接获取
        return div_list


class Write(object):
    """
    获取将更新后的内容写入的目标文件名
    name : 需要写入的目标文件名
    id_frm :
    feature_frm :
    """
    def __init__(self, name, id_frm, feature_frm):
        self.name = name
        self.id_frm = id_frm
        self.feature_frm = feature_frm

    def write(self):
        root = {'id_frm': self.id_frm, 'feature_frm': self.feature_frm}
        with open(self.name, 'wb') as file:
            pickle.dump(root, file)
        print('写入成功')


class Delete(object):
    """
    执行删除操作
    1. 需要明确我们需要删除哪些：div_cc,div_c_t,div_cc2,div_c_t2
    """
    def __init__(self, div_cc, div_c_t, div_cc2, div_c_t2, div_tt):
        self.div_cc = div_cc
        self.div_cc2 = div_cc2
        self.div_c_t = div_c_t
        self.div_c_t2 = div_c_t2
        self.div_tt = div_tt

    def div_del(self):
        print('\n全部完成，下面就是执行删除部分')
        # 求出交集，也即是需要在div_cc中删除的id_div
        del_id_div = [i for i in list(self.div_cc['id_div']) if i in list(self.div_tt['id_div'])]

        # 根据求出的del_id_div,求出我们需要的del_id_div_cc
        del_id_div_cc = []
        for i in self.div_cc.index:
            if self.div_cc.loc[i, 'id_div'] in del_id_div:
                del_id_div_cc.append(i)

        # 根据求出的del_id_div_cc,求出我们需要的del_id_div_c_t
        del_id_div_c_t = []
        for i in self.div_c_t.index:
            if self.div_c_t.loc[i, 'id_div_cc'] in del_id_div_cc:
                del_id_div_c_t.append(i)

        # 到此我们求出了需要删除的id_div,id_div_cc,id_div_c_t他们的id列表
        # 下面需要进行删除操作的表有：div_cc,div_c_t,div_c_t2,div_cc2
        # 鉴于index的不可更改性，所以我们只能新建一个副本，然后再引用

        # 删除div_cc
        self.div_cc = self.div_cc.drop(del_id_div_cc)
        copy_div_cc = DataFrame({'id_div': []})
        copy_div_cc.index.name = 'id_div_cc'
        copy_div_cc = copy_div_cc.reindex(range(len(self.div_cc)))
        for i, j in zip(self.div_cc.index, copy_div_cc.index):
            copy_div_cc.loc[j, 'id_div'] = self.div_cc.loc[i, 'id_div']
        # 执行完上述的步骤，我们就已经得到了想要的div_cc了，只需要重新引用就可以了
        self.div_cc = copy_div_cc

        # 删除div_c_t
        self.div_c_t = self.div_c_t.drop(del_id_div_c_t)
        copy_div_c_t = DataFrame({'id_div_cc': []})
        copy_div_c_t.index.name = 'id_div_c_t'
        copy_div_c_t = copy_div_c_t.reindex(range(len(self.div_c_t)))
        for i, j in zip(self.div_c_t.index, copy_div_c_t.index):
            copy_div_c_t.loc[j, 'id_div_cc'] = self.div_c_t.loc[i, 'id_div_cc']
        self.div_c_t = copy_div_c_t

        # 删除div_cc2
        self.div_cc2 = self.div_cc2.drop(del_id_div_cc)
        copy_div_cc2 = DataFrame({'height': [], 'width': []})
        copy_div_cc2.index.name = 'id_div_cc'
        copy_div_cc2 = copy_div_cc2.reindex(range(len(self.div_cc2)))
        for i, j in zip(self.div_cc2.index, copy_div_cc2.index):
            copy_div_cc2.loc[j, 'height'] = self.div_cc2.loc[i, 'height']
            copy_div_cc2.loc[j, 'width'] = self.div_cc2.loc[i, 'width']
        # 执行完上述的步骤，我们就已经得到了想要的div_cc了，只需要重新引用就可以了
        self.div_cc2 = copy_div_cc2

        # 删除div_c_t2
        self.div_c_t2 = self.div_c_t2.drop(del_id_div_c_t)
        copy_div_c_t2 = DataFrame({'x_value': [], 'y_value': [], 'string': []})
        copy_div_c_t2.index.name = 'id_div_c_t'
        copy_div_c_t2 = copy_div_c_t2.reindex(range(len(self.div_c_t)))
        for i, j in zip(self.div_c_t2.index, copy_div_c_t2.index):
            copy_div_c_t2.loc[j, 'x_value'] = self.div_c_t2.loc[i, 'x_value']
            copy_div_c_t2.loc[j, 'y_value'] = self.div_c_t2.loc[i, 'y_value']
            copy_div_c_t2.loc[j, 'string'] = self.div_c_t2.loc[i, 'string']
        self.div_c_t2 = copy_div_c_t2

        div_list = [self.div_cc, self.div_cc2, self.div_c_t, self.div_c_t2]
        return div_list
















