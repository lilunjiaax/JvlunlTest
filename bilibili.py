
"""
1+2i
2+i


0+5i

"""

# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     fushu1 = sys.stdin.readline().strip().replace('i', '')
#     fushu2 = sys.stdin.readline().strip().replace('i', '')
#     a_list1 = [int(i) if i else 1 for i in fushu1.split('+')]
#     a_list2 = [int(i) if i else 1 for i in fushu2.split('+')]
#     a_list3 = [a_list1[0]*a_list2[0] - a_list1[1]*a_list2[1], a_list1[0]*a_list2[1]+a_list1[1]*a_list2[0]]
#     a_str = "{}+{}i".format(a_list3[0], a_list3[1])
#     print(a_str)




"""
2004-03-01


61
31 + 
"""

# def count_func(year, month, day):
#     count = 0
#     if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#         li1 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#         for i in range(month - 1):
#             count += li1[i]
#         return count + day
#     else:
#         li2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#         for i in range(month - 1):
#             count += li2[i]
#         return count + day
#
# import sys
# if __name__ == "__main__":
#     s = sys.stdin.readline().strip()
#     year, month, day = [int(i) for i in s.split("-")]
#     print(count_func(year, month, day))


def func_pop(a_list, count):
    while count:
        a_list.pop(0)
        count -= 1


import sys
if __name__ == "__main__":
    s = sys.stdin.readline().strip().replace('#', '')
    count = int(input())
    s = s.strip()
    a_list = [int(i) for i in s.split(" ")]
    des_list = []
    while len(a_list) > count:
        tmp = a_list[:count]
        tmp.reverse()
        des_list.extend(tmp)
        func_pop(a_list, count)
    des_list.extend(a_list)
    a_str = '{}'.format(des_list[0])
    for i in des_list[1:]:
        a_str += '->{}'.format(i)
    print(a_str)
