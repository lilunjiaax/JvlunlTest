#
# import sys
#
# a_length = int(sys.stdin.readline().strip())
# a_str = sys.stdin.readline().strip()
# des = int(sys.stdin.readline().strip())
#
# a_list = [int(i) for i in a_str.split(' ')]
# a_list.sort()
#
#
# def func1(a_list, des, a_length):
#     count = 0
#     if a_list[0] >= des:
#         return count
#     for i in range(a_length):
#         if des < a_list[i]:
#             break
#         for j in range(i+1, a_length):
#             if des <= a_list[i] + a_list[j]:
#                 break
#             a_minus = des - a_list[i] - a_list[j]
#             for k in range(j+1, a_length):
#                 if a_list[k] < a_minus:
#                     count += 1
#     return count
#
#
# print(func1(a_list, des, a_length))




"""
输入
3
1 1
2 1
3 1

输出
4 1
"""
# import sys
# if __name__ == "__main__":
#     n = int(sys.stdin.readline().strip())
#     line_list = [[0, 0]]
#     for i in range(n):
#         line = sys.stdin.readline().strip()
#         values = list(map(int, line.split()))
#         line_list.append(values)
#     max_count = 0
#     task_count = 0
#     time = 0
#     jiange = line_list[1][0] - line_list[0][0]
#     i = 1
#     while i < n+1:
#         time += jiange
#         task_count += line_list[i][1]
#         if task_count > max_count:
#             max_count = task_count
#         # 开始执行任务
#         if i+1 >= n+1:
#             break
#         jiange = line_list[i+1][0] - line_list[i][0]
#         if jiange > task_count:
#             task_count = 0
#         else:
#             task_count -= jiange
#         i += 1
#     if task_count > 0:
#         time += task_count
#     print("{} {}".format(time, max_count))


def func1(values):
    if len(values) == 2:
        return values.index(max(values))
    if len(values) == 1:
        return 0
    if values[0] >= values[1] and values[-1] <= values[-2]:
        return 0
    if values[-1] >= values[-2] and values[0] <= values[1]:
        return -1
    if values[0] >= values[1] and values[-1] >= values[-2]:
        if values[0] - values[1] > values[-1] - values[-2]:
            return 0
        elif values[0] - values[1] < values[-1] - values[-2]:
            return -1
        else:
            if values[0] > values[-1]:
                return 0
            else:
                return -1
    if values[0] <= values[1] and values[-1] <= values[-2]:
        if values[1] - values[0] > values[-2] - values[-1]:
            return -1
        elif values[1] - values[0] < values[-2] - values[-1]:
            return 0
        else:
            if values[0] > values[-1]:
                return 0
            else:
                return -1

import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    me_list = []
    laoren_list = []
    # 我先取
    while values:
        me_list.append(values.pop(func1(values)))
        if values:
            laoren_list.append(values.pop(func1(values)))
    print(sum(me_list))







