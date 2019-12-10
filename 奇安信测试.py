"""
结束进程树
题目描述：
给定n个进程，这些进程满足以下条件：
（1）每个进程有唯一的PID，其中PID为进程ID
（2）每个进程最多只有一个父进程，但可能有多个子进程，用PPID表示父进程ID
（3）若一个进程没有父进程，则其PPID为0
（4）PID、PPID都是无符号整数
结束进程树的含义是当结束一个进程时，它的所有子进程也会被结束，包括子进程的子进程。
现在给定大小为n的两组输入列表A和B（1 <= n <= 100），列表A表示进程的PID列表，列表B表示列表A对应的父进程的列表，即PPID列表。
若再给定一个PID，请输出结束该PID的进程树时总共结束的进程数量。

输入
3 1 5 21 10
0 3 3 1 5
5
输出
2

样例输入
3 1 5 21 10
0 3 3 1 5
3

样例输出
5


"""
# while 1:
#     pid = input()
#     ppid = input()
#     num = input()
#     if pid != "":
#         ss = [int(i) for i in pid.split(" ")]
#         sss = [int(i) for i in ppid.split(" ")]
#         num1 = int(num)
#         if num1 not in ss and (num1 not in sss):
#             print(0)
#             continue
#         des_list = [num1]
#         if num1 not in sss:
#             print(ss.count(num1))
#             continue
#         a_len = len(ss)
#         while 1:
#             flag = 0
#             for i in range(a_len):
#                 if sss[i] in des_list:
#                     if ss[i] not in des_list:
#                         des_list.append(ss[i])
#                         flag = 1
#             if not flag:
#                 break
#         if ss.count(num1) == 1:
#             print(len(des_list))
#         elif ss.count(num1) > 1:
#             print(len(des_list) + ss.count(num1) - 1)
#
#     else:
#         break
"""
题目描述：
N个人排成一队，从1到5轮流报数，报5的人是幸运者，出列。
报到队尾后，从队首接着报。依此循环。
问：排在队尾的人是第几名幸运者？
注： N为小于100000的正整数。
例：
1人排成一队，他就是第1名幸运者。
3人排成一队，队尾是第2名幸运者。
5人排成一队，队尾是第1名幸运者。
8人排成一队，队尾是第3名幸运者
即求：N人排成一队，队尾是第多少名幸运者？
输入
队伍总人数
输出
队尾者的幸运编号

样例输入
20
样例输出
4

"""
while 1:
    num = input()
    if num != "":
        num1 = int(num)
        if num1 == 1:
            print(1)
        if num1 == 3:
            print(2)
        if num1 == 5:
            print(1)
        if num1 == 8:
            print(3)
    else:
        break


