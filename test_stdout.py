"""
样例输入
81 4
2 2

样例输出
94.73
3.41

"""
import sys


# while 1:
#     s = input()
#     if s != "":
#         m, n = [int(j) for j in s.split(' ')]
#         a_list = [m]
#         while len(a_list) != n:
#             m = m ** 0.5
#             a_list.append(m)
#         sum_list = round(sum(a_list), 2)
#         print(sum_list)
#     else:
#         break

"""
样例输入
100 120
300 380

样例输出
no
370 371
"""
# def judge(num):
#     a = num % 10
#     b = num // 10 % 10
#     c = num // 100
#     if num == a**3 + b**3 + c**3:
#         return True
#     else:
#         return False
#
# while 1:
#     s = input()
#     if s != '':
#         min, max = [int(j) for j in s.split(' ')]
#         a_list = []
#         while min <= max:
#             if judge(min):
#                 a_list.append(min)
#             min += 1
#         if len(a_list) == 0:
#             print('no')
#         else:
#             j = 0
#             for i in a_list:
#                 if j == 0:
#                     sys.stdout.write(str(i))
#                     j += 1
#                 else:
#                     sys.stdout.write(' ' + str(i))
#             print('')
#     else:
#         break

# import sys
# if __name__ == "__main__":
#     a_str = sys.stdin.readline().strip()
#     a_list = a_str.split(",")
#     resu_dict = []
#     for i in a_list:
#         if i[-1] in ['d', 'e']:
#             if i in resu_dict:
#                 resu_dict[i] += 1
#             else:
#                 resu_dict[i] = 1
#     resu_str = '{'
#     for i in resu_dict:
#         resu_dict = resu_str + i + '=' + str(resu_dict[i]) + ', '
#     print(resu_str[:-2]+'}')



import sys
if __name__ == "__main__":
    a_str = sys.stdin.readline().strip()
    a_list = [i for i in a_str]
    a_len = len(a_list)
    i = 0
    resu_dict = {}
    while i < a_len:
        count = 1
        while i+1 < a_len and (a_list[i+1] == a_list[i]):
            count += 1
            i += 1
        if count == 1:
            continue
        else:
            if a_list[i] in resu_dict:
                resu_dict[a_list[i]] += count
            else:
                resu_dict[a_list[i]] = count
    print(resu_dict)

import sys
if __name__ == "__main__":
    a_str = sys.stdin.readline().strip()
    a_list = [i for i in a_str]
    a_len = len(a_list)
    i = 0
    resu_dict = {}
    while i < a_len:
        count = 1
        while i+1 < a_len and (a_list[i+1] == a_list[i]):
            count += 1
            i += 1
        if count == 1:
            i += 1
            continue
        else:
            if a_list[i] in resu_dict:
                resu_dict[a_list[i]] += count
            else:
                resu_dict[a_list[i]] = count
            i += 1
    tmp = sorted(resu_dict.items(), key=lambda x:x[1], reverse=True)
    for item in tmp:
        print('{}:{}'.format(item[0], item[1]))

# import sys
# if __name__ == "__main__":
#     a_str = sys.stdin.readline().strip()
#     a_list = a_str.split(",")
#     a_set = []
#     for i in a_list:
#         tmp = set([j for j in i])
#         a_set.append(tmp)
#     resu_dict = []
#     for i in a_set:
#         if i[-1] in ['d', 'e']:
#             if i in resu_dict:
#                 resu_dict[i] += 1
#             else:
#                 resu_dict[i] = 1
#     resu_str = '{'
#     for i in resu_dict:
#         resu_dict = resu_str + i + '=' + str(resu_dict[i]) + ', '
#     print(resu_str[:-2]+'}')





