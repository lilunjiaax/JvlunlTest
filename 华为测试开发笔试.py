#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
# import sys
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))

#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
# import sys
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         # 把每一行的数字分隔后转化成int列表
#         values = list(map(int, line.split()))
#         for v in values:
#             ans += v
#     print(ans)


# import sys
# n = sys.stdin.readline().strip()
# values = list(map(int, n.split()))
# a_len = len(values)
# count = 100
#
# def func1(i, values, a_len):
#     a_index = i
#     count = 1
#     while a_index < (a_len-1):
#         a_index = values[a_index] + a_index
#         count += 1
#     if a_index == (a_len - 1):
#         return count
#     else:
#         return -1
# for i in range(1, a_len//2):
#     tmp = func1(i, values, a_len)
#     if tmp == -1:
#         continue
#     elif tmp < count:
#         count = tmp
# if count == 100:
#     print(-1)
# else:
#     print(count)
#
# import sys
#
# sys.setrecursionlimit(100000)
# n = sys.stdin.readline().strip()
# values = list(map(int, n.split()))
# n, m = values
#
# a_list = [i for i in range(1, n+1)]
#
# def per(a_list, m):
#     res = []
#     count = 0
#     a_sum = m
#     digui(a_list, res, '', count, a_sum)
#     return sorted(res)
#
# def digui(a_list, res, path, count, a_sum):
#     if count == a_sum:
#         res.append(path)
#     else:
#         for i in range(len(a_list)):
#             digui(a_list, res, path + str(a_list[i]), count+1, a_sum)
#
#
# a_list = per(a_list, m)
# b_list = []
# for i in a_list:
#     b_list.append(sorted([int(j) for j in i]))
#
# c_list = []
# for i in b_list:
#     c_list.append(''.join(list(map(str, i))))
#
# print(len(set(c_list)) % 1000000007)

"""
[1234]=[12]+[34]*{50},[12]=[1]+[2]/{2};[1]=10,[2]=20,[34]=50;[1234]

"""
# import sys
# gongshi, value, des = sys.stdin.readline().strip().split(";")
# value_dict = {}
# for i in value.split(','):
#     a, b = i.split("=")
#     value_dict[a] = int(b)
#
# gongshi_dict = {}
# for i in gongshi.split(","):
#     a, b = i.split("=")
#     tmp = [j for j in b.split("]")]
#     gongshi_dict[a] = tmp

import sys
line = sys.stdin.readline().strip()
a_len = len(line)
a_dict = {'1': 'A',
          '2': 'B',
          '3': 'C',
          '4': 'D',
          '5': 'E',
          '6': 'F',
          '7': 'G',
          '8': 'H',
          '9': 'I',
          '10': 'J',
          '11': 'K',
          '12': 'L',
          '13': 'M',
          '14': 'N',
          '15': 'O',
          '16': 'P',
          '17': 'Q',
          '18': 'R',
          '19': 'S',
          '20': 'T',
          '21': 'U',
          '22': 'V',
          '23': 'W',
          '24': 'X',
          '25': 'Y',
          '26': 'Z'
          }
resu_list = [[0, '']]

# while 1:
#     flag = 0
#     tmp_list = []
#     for item in resu_list:
#         if item[0] < a_len:
#
#
#     if not flag:
#         break



# a_sum = 0
#
# a_len_tree = len(empHierarchy)
# for i in range(a_len_tree):
#     if empHierarchy[i] == -1:
#         continue
#     # 判定他是老员工，且2*i +1 2*i +2的值都是-1
#     if (empHierarchy[2*i+1] == -1 or 2*i+1>=a_len_tree) and (empHierarchy[2*i+2] == -1 or 2*i+2>=a_len_tree) and (i%2 == 1):
#         a_sum += employeeReputions[employeeIDs.index(empHierarchy[i])]
#
# print(a_sum)
    
        








































