import sys
from pandas import DataFrame
# 从公共模块中导入读取类，删除类，写入类
from means import Read, Write, Delete

''' 执行方法：python pro2v2.py problem2.pk aim_name.pk '''


def find(div, num, key):
    """
    div:DataFrame
    num:col值
    key:（0，1） == （div_cc,div_c_t）
    """
    list1 = []
    # 寻到的index值都注入到列表中，通过判断len(list)来得出结论
    if key == 0:
        col = 'id_div'
    elif key == 1:
        col = 'id_div_cc'
    for i in div.index:
        if div.loc[i, col] == num:
            list1.append(i)
    return list1


# 判断遍历到的id_div是否指向div_cc
# 处于div_cc中,**注意：同时不能在div_tt里面
def judge(i, div_cc, div_tt):
    a = 0
    for k in div_cc['id_div']:
        if k == i:
            a = 1
    for k in div_tt['id_div']:
        if k == i:
            a = 0
    if a == 1:
        return True
    else:
        return False


def print_info(div, div2, div_cc, div_tt):
    print('div标签的个数：', end='')
    print(len(div))
    print('div2标签的个数：', end='')
    print(len(div2))
    print('div_cc标签的个数：', end='')
    print(len(div_cc))
    print('div_tt标签的个数：', end='')
    print(len(div_tt))
    print('---------------------------')


def main():
    file_name = sys.argv[1]
    aim_name = sys.argv[2]
    # 实例化读取类
    read = Read(file_name)
    # 解包接收返回的结果
    div, div_cc, div_tt, div_c_t, div2, div_cc2, div_c_t2 = read.read()
    print_info(div, div2, div_cc, div_tt)
    print('统计每个div_cc里面包含有多少个div_c_t的结果(请稍等):')
    while True:
        flag = 0
        for i in div2.index:
            # i 代表了div2里面的index:id_div
            if i < list(div_tt['id_div'])[-1] and judge(i, div_cc, div_tt):  # 选出需要拆分的div_cc标签对应的id_div为 i
                flag = 1  # 修改标志值，说明还进去处理过了
                count = 0
                '''根据id_div找出对应的div_cc,再根据div_cc找出对应的div_c_t(可能有多个)'''
                id_div = i

                # 需要提前把需要用到的(div,div2里面的值读出来)
                id_page = div.loc[id_div, 'id_page']
                x_value = div2.loc[id_div, 'x_value']
                y_value = div2.loc[id_div, 'y_value']

                # 返回的list一定只有一个值，因为id_div,id_div_cc是一一对应的
                id_div_cc = find(div_cc, id_div, 0)[0]
                id_div_c_t_list = find(div_c_t, id_div_cc, 1)
                sum1 = len(id_div_c_t_list)
                # 输出每个div_cc里面包含的div_c_t的个数，用于检测调试
                print(' ' + str(sum1) + ' ', end='')

                for j in id_div_c_t_list:
                    '''得到的每一个 j 都是id_div_c_t'''
                    count = count + 1
                    if count == 1:
                        '''说明此时处理的是div_cc里面的第一个div_c_t'''
                        c_t_x = div_c_t2.loc[j, 'x_value']
                        c_t_y = div_c_t2.loc[j, 'y_value']
                        # c_t_x = div_c_t2['x_value'][i]
                        # c_t_y = div_c_t2['y_value'][i]
                        # 更新div2里面的值，写入div_tt里面一条记录
                        div2.loc[id_div, 'x_value'] = x_value + c_t_x
                        div2.loc[id_div, 'y_value'] = y_value + c_t_y
                        # 给div_tt添加映射id_div
                        # div_tt = div_tt.append(DataFrame({'id_div': [id_div]}), ignore_index=True)
                        # 给div_tt添加记录不再像代码1中很方便，第一次添加需要移动修改
                        # 第二次往后添加需要移动，加1来空出一行
                        for k in range(len(div_tt), 0, -1):
                            if div_tt.loc[k - 1, 'id_div'] > id_div:
                                div_tt.loc[k, 'id_div'] = div_tt.loc[k - 1, 'id_div']
                            else:
                                '''当不成立时 k 就已经处于我们需要插入的那个位置了'''
                                div_tt.loc[k, 'id_div'] = id_div
                                break
                        # 上述就是第一次插入div_tt的过程

                    elif (count <= sum1) and (count > 1):
                        id_div += 1
                        '''这样的限定条件暗示了不是第一个div_c_t了'''
                        c_t_x = div_c_t2.loc[j, 'x_value']
                        c_t_y = div_c_t2.loc[j, 'y_value']

                        for k in range(len(div2), id_div, -1):
                            div2.loc[k, 'x_value'] = div2.loc[k - 1, 'x_value']
                            div2.loc[k, 'y_value'] = div2.loc[k - 1, 'y_value']

                        # 给id_div指定的那一行赋值
                        div2.loc[id_div, 'x_value'] = x_value + c_t_x
                        div2.loc[id_div, 'y_value'] = y_value + c_t_y

                        # ------------------------------------------------------------
                        # 本质上向下移动了一行，会导致一部分的div_cc的id_div变大了1,所以针对
                        # div_cc表，对于所有id_div>=我们本次添加的id_div,需要给他们多加1才可以。
                        # 对div_cc的id_div进行修改
                        for k in div_cc.index:
                            if div_cc.loc[k, 'id_div'] >= id_div:
                                div_cc.loc[k, 'id_div'] += 1

                        # 对div_tt进行调整和添加
                        for k in div_tt.index:
                            if div_tt.loc[k, 'id_div'] >= id_div:
                                div_tt.loc[k, 'id_div'] += 1

                        for k in range(len(div_tt), 0, -1):
                            if div_tt.loc[k - 1, 'id_div'] > id_div:
                                div_tt.loc[k, 'id_div'] = div_tt.loc[k - 1, 'id_div']
                            else:
                                '''当不成立时 k 就已经处于我们需要插入的那个位置了'''
                                div_tt.loc[k, 'id_div'] = id_div
                                break

                        # 给div表添加一个数据(id_div,id_page)
                        # div表和div2表在index上应该是完全一致的
                        for k in range(len(div), id_div, -1):
                            div.loc[k, 'id_page'] = div.loc[k - 1, 'id_page']
                        div.loc[id_div, 'id_page'] = id_page

        if flag == 0:
            break

    # 下面就是解决删除问题：
    '''
    1. 首先确定指标问题：我以什么为标准进行删除
    2. 遍历div_tt里面的的id_div,明确里面的内容，有div_cc直接改为div_tt的，也有多余的div_c_t添加到div_tt里面的，
    3. div_tt里面的id_div与div_cc里面的id_div是交集关系，相交的那一部分就是我们要删除的div_cc对应的id_div
    '''
    # 实例化删除类
    div_del = Delete(div_cc, div_c_t, div_cc2, div_c_t2, div_tt)
    div_cc, div_cc2, div_c_t, div_c_t2 = div_del.div_del()
    print('删除执行完毕，最终统计结果为：')
    print_info(div, div2, div_cc, div_tt)
    # 实例化重写文件类
    # 在主函数的开始我们就已经获取了aim_name
    id_frm = {'div': div, 'div_cc': div_cc, 'div_tt': div_tt, 'div_c_t': div_c_t}
    feature_frm = {'div': div2, 'div_cc': div_cc2, 'div_c_t': div_c_t2}
    write = Write(aim_name, id_frm, feature_frm)
    write.write()


if __name__ == '__main__':
    main()

