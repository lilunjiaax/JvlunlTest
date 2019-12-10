"""
题目描述：
你现在在(0,0)，需要到(x,y)去，路上有n个障碍物。给出每个障碍物的坐标，你只能平行于坐标轴走整数步，问你最少需要多少步才能走到目的地。

输入
第一行三个数x,y,n
接下来n行，每行描述一个障碍物的坐标x_i,y_i
-500≤x,y,x_i,y_i≤500
n≤10000
保证有解

输出
输出一个数，代表最少的步数。


样例输入
2 0 3
1 0
1 1
1 -1

样例输出
6

"""


#
# while 1:
#     s = input().strip()
#     if s != '':
#         a, b, c = [int(i) for i in s.split()]
#         des = [a, b]
#         start = [0, 0]
#         node_list = []
#         for i in range(c):
#             s = input().strip()
#             node_list.append([int(i) for i in s.split()])
#         count = 0
#         while 1:
#             if start[0] == des[0] and start[1] == des[1]:
#                 break
#             if des[0] > start[0]:
#                 tmp_x = start[0] + 1
#             elif des[0] < start[0]:
#                 tmp_x = start[0] - 1
#             else:
#                 tmp_x = start[0]
#             if des[1] > start[1]:
#                 tmp_y = start[1] + 1
#             elif des[1] < start[1]:
#                 tmp_y = start[1] - 1
#             else:
#                 tmp_y = start[1]
#             if [tmp_x, tmp_y] in node_list:
#
#
#
#         print(count)
#     else:
#         break


"""
题目描述：
西西所在的国家有N座城市，每座城市都有一道传送门，城市 i 的传送门通往城市 a[i]。当西西位于城市 i 时，每次他可以执行以下三种操作中的一种：
l 花费 A 的费用，从城市 i 前往城市 a[i]；
l 如果 a[i] > 1，可以花费 B 的费用，将 a[i] 的值减少 1；
l 如果 a[i] < N，可以花费 C 的费用，将 a[i] 的值增加 1。
现在，西西想从城市 1 前往城市 N，那么他至少要花费多少费用？

输入
第一行输入四个整数 N、A、B、C（1 < N <= 10000，1 <= A、B、C <= 100000）。
第二行输入 N 个整数 a[1] 到 a[N]（1 <= a[i] <= N）。

输出
输出一个整数，表示从城市 1 前往城市 N 所花费的最少费用。


样例输入
7  1  1  1
3  6  4  3  4  5  6
样例输出
4

提示
样例解释
西西可以按顺序执行以下操作：
将 a[1] 减少 1，此时 a[1] = 2； 
从城市 1 前往城市 2；
将 a[2] 增加 1，此时 a[2] = 7；
从城市 2 前往城市 7。
"""

# while 1:
#     s = input().strip()
#     if s != '':
#         N, A, B, C = [int(i) for i in s.split()]
#         s1 = input().strip()
#         city_list = [0]
#         city_list.extend([int(i) for i in s1.split()])
#         count = 0
#         while 1:
#             if N-1:
#                 pass
#
#
#
#
#     else:
#         break

def func(k, a_list):
    count = 0
    k_list = a_list[k[0]-1:k[1]]
    for i in k_list:
        if k_list.count(i) == 1:
            count += 1
    return count


while 1:
    s= input().strip()
    if s != '':
        n = int(s)
        n_list = [int(i) for i in input().strip().split()]
        m = int(input().strip())
        a_list = []
        for i in range(m):
            a_list.append([int(i) for i in input().strip().split()])

        for k in a_list:
            print(func(k, n_list))
    else:
        break














