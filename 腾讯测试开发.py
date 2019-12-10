
# import sys
# count = int(sys.stdin.readline().strip())
# flag = 0
# for line in sys.stdin:
#     if flag == 0:
#         a_len = int(line)
#         if a_len < 11:
#             print("NO")
#             next_flag = 0
#             flag = 1
#         else:
#             next_flag = a_len
#     else:
#         if next_flag == 0:
#             flag = 0
#             continue
#         else:
#             tmp = 0
#             for i in line:
#                 if i == '8':
#                     break
#                 tmp += 1
#             flag = 0
#             if next_flag - tmp >= 11:
#                 print('YES')
# import sys
# count = int(sys.stdin.readline().strip())
# flag = 0
# a_list = []
#
# count *= 2
# a_len = count
# while count:
#
#     if count == 0:
#         break
#     a_list.append(sys.stdin.readline().strip())
#     count -= 1
#
# a1 = []
# a2 = []
# for i in range(0, a_len, 2):
#     a1.append(a_list[i])
# for j in range(1, a_len, 2):
#     a2.append(a_list[j])
# a_len = len(a1)
# for i in range(a_len):
#     if int(a1[i]) < 11:
#         print('NO')
#         continue
#     else:
#         tmp = 0
#         for j in a2[i]:
#             if j == '8':
#                 break
#             tmp += 1
#         if int(a1[i]) - tmp >= 11:
#             print('YES')
#         else:
#             print('NO')

# import sys
# count = int(sys.stdin.readline().strip())
#
# a_list = []
# while count:
#     if count == 0:
#         break
#     a = [int(i) for i in sys.stdin.readline().strip().split()]
#     for i in range(a[0]):
#         a_list.append(a[1])
#     count -= 1
#
# a_len = len(a_list)
# a_list.sort()
# a_index = 0
# tmp = 0
# while a_index < a_len/2:
#     tmp1 = a_list[a_index] + a_list[a_len - a_index - 1]
#     if tmp1 > tmp:
#         tmp = tmp1
#     a_index += 1
#
# print(tmp)


"""
2
4
5 9 4 7
8
9 13 18 10 12 4 18 3

"""


# import sys
# count = int(sys.stdin.readline().strip())
# flag = 0
# a_list = []
# count *= 2
# while count:
#     if count == 0:
#         break
#     a_list.append(sys.stdin.readline().strip())
#     count -= 1
#
# a1 = []
# for j in range(1, len(a_list), 2):
#     a1.append([int(i) for i in a_list[j].split()])
#
# for i in a1:
#     j = sorted(i)
#     tmp1 = 0
#     tmp2 = 0
#     a_len = len(j)
#     if (a_len // 2) % 2 == 0:
#         for k in range(a_len // 2):
#             if k % 2 == 0:
#                 tmp1 += j[k] + j[a_len - k - 1]
#             else:
#                 tmp2 += j[k] + j[a_len - k - 1]
#         if a_len % 2 == 1:
#             if tmp1 < tmp2:
#                 tmp1 += j[a_len // 2]
#             else:
#                 tmp2 += j[a_len // 2]
#     else:
#         if a_len % 2 == 0:
#             km = (a_len-1) // 2
#         else:
#             km = (a_len-2) // 2
#         for k in range(km):
#             if k % 2 == 0:
#                 tmp1 += j[k] + j[a_len - k - 1]
#             else:
#                 tmp2 += j[k] + j[a_len - k - 1]
#         if a_len % 2 == 0:
#             if tmp1 < tmp2:
#                 tmp1 += j[a_len // 2]
#                 tmp2 += j[a_len // 2 - 1]
#             else:
#                 tmp2 += j[a_len // 2]
#                 tmp1 += j[a_len // 2 - 1]
#         else:
#             if tmp1 < tmp2:
#                 tmp1 += j[a_len // 2 + 1]
#                 tmp2 += j[a_len // 2]
#             else:
#                 tmp2 += j[a_len // 2+1]
#                 tmp1 += j[a_len // 2]
#             if tmp1 < tmp2:
#                 tmp1 += j[a_len//2 - 1]
#             else:
#                 tmp2 += j[a_len//2 - 1]
#     if tmp1 < tmp2:
#         print(tmp1, end=' ')
#         print(tmp2)
#     else:
#         print(tmp2, end=' ')
#         print(tmp1)


# import sys
# a = sys.stdin.readline().strip()
# b = sys.stdin.readline().strip()
# a_len = len(a)
# b_len = len(b)
# def func1(i, b_len, a, b):
#     try:
#         if a.index(b) == 0:
#             return True
#     except:
#         return False
#     return False
# count = 0
# for i in range(a_len):
#     if func1(i, b_len, a[i:], b):
#         count += 1
# print(count)


import sys
a, b = [int(i) for i in sys.stdin.readline().strip().split()]



