# import sys
#
# a = int(sys.stdin.readline().strip())
# a_list = []
# while a:
#     tmp = int(sys.stdin.readline().strip())
#     a_list.append(tmp)
#     a -= 1
#
#
# def func1(i):
#     tmp_list = []
#     tmp_str = ''
#     while i > 9:
#         tmp_list.append(9)
#         i -= 9
#     tmp_list.append(i)
#     tmp_list.reverse()
#     for j in tmp_list:
#         tmp_str += str(j)
#     return int(tmp_str)
#
# for i in a_list:
#     print(func1(i))

"""
2 
13
18
"""


"""
2
1 2 3
1 2 6

"""
import sys
a = int(sys.stdin.readline().strip())
a_list = []
while a:
    tmp = [int(j) for j in sys.stdin.readline().strip().split()]
    a_list.append(tmp)
    a -= 1

def func1(b_list):
    a = 0
    b = 0
    c = 0
    while sum(b_list):
        if b_list[0] + b_list[1] > 0:
            a += 1
            if b_list[0] > b_list[1]:
                b_list[0] -= 1
            else:
                b_list[1] -= 1

        if b_list[1] + b_list[2] > 0:
            b += 1
            if b_list[1] > b_list[2]:
                b_list[1] -= 1
            else:
                b_list[2] -= 1

        if b_list[0] + b_list[2] > 0:
            c += 1
            if b_list[0] > b_list[2]:
                b_list[0] -= 1
            else:
                b_list[2] -= 1
    return max(a, b, c)
for i in a_list:
    print(func1(i))



"""
2
5
1 3 9 2 6
5
4 2 9 16 7
"""
# import sys
# a = int(sys.stdin.readline().strip())
# a_list = []
# count1 = a
# a *= 2
# count = a
# while a:
#     tmp = [int(j) for j in sys.stdin.readline().strip().split()]
#     a_list.append(tmp)
#     a -= 1
# a1_list = []
# for i in range(1, count, 2):
#     a1_list.append(a_list[i])
# a2_list = []
# for i in range(0, count, 2):
#     a2_list.append(a_list[i][0])
# def func1(a_len, b_list):
#     tmp_list = []
#     tmp = 0
#     for i in range(a_len):
#         if b_list[i] > sum(tmp_list):
#             tmp_list.append(b_list[i])
#         else:
#             if len(tmp_list) > tmp:
#                 tmp = len(tmp_list)
#             tmp_list = []
#             tmp_list.append(b_list[i])
#
#     return tmp
#
#
# for i in range(count1):
#     print(func1(a2_list[i], a1_list[i]))



"""
1 
6
1 2 3 4 5 6
"""
# import sys
# a = int(sys.stdin.readline().strip())
# a_list = []
# count1 = a
# a *= 2
# count = a
# while a:
#     tmp = [int(j) for j in sys.stdin.readline().strip().split()]
#     a_list.append(tmp)
#     a -= 1
# a1_list = []
# for i in range(1, count, 2):
#     a1_list.append(a_list[i])
# a2_list = []
# for i in range(0, count, 2):
#     a2_list.append(a_list[i][0])
#
# def func1(a_len, b_list):
#     a_sum = sum(b_list)
#     if a_sum % 2 == 1:
#         return "NO"
#     b_list.extend(b_list)
#     tmp = a_sum // 2
#     for j in range(a_len):
#         count = 0
#         for i in range(j+1, len(b_list)):
#             count += 1
#             tmp1 = sum(b_list[j:i])
#             if tmp1 < tmp:
#                 continue
#             if tmp1 > tmp:
#                 break
#             if tmp1 == tmp:
#                 return "YES"
#             if count >= a_len:
#                 break
#     return "NO"
#
#
# for j in range(count1):
#     print(func1(a2_list[j], a1_list[j]))

