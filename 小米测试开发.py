"""
一行由正整数组成的数字字符串，和一个正整数 K，两个数据由英文逗号隔开，如：1432219,3。

输出
移除 K 位后可能的最小的数字字符串。

如 1432219 移除 4, 3, 2 这 3 个数字后得到 1219，为所有可能中的最小值。


样例输入
1432219,3
样例输出
1219

"""



# while 1:
#     s = input().strip()
#     if s != '':
#         s = s.split(',')
#         m = s[0]
#         n = s[1]
#         a_list = list(m)
#         flag = 0
#         for _ in range(int(n)):
#             for i in range(flag, len(a_list) - 1):
#                 if int(a_list[i]) > int(a_list[i + 1]):
#                     a_list.remove(a_list[i])
#                     flag = i - 1 if i - 1 > 0 else 0
#                     break
#
#                 elif i == len(a_list) - 2:
#                     a_list.remove(a_list[-1])
#                     flag -= 1
#         if len(a_list) > 1:
#             while a_list[0] == "0":
#                 a_list.remove("0")
#         elif not a_list:
#             a_list = ["0"]
#         else:
#             pass
#         print("".join(a_list))
#
#     else:
#         break

"""
题目描述：
证券股票价格时时刻都在起伏不定，变幻莫测，如何保证得到最高收益是每个投资人最终追求，
现在模拟给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

输入
输入一个数组，里面包含整形数字，用来模拟价格的起伏。

输出
 算出价格区间内的最高收益，如果没有收益，则按照0计算


样例输入
[7,1,4,3,1]
样例输出
3

"""


while 1:
    s = input().strip()
    if s != '':
        s = [int(j) for j in s.replace('[', '').replace(']', '').replace(',', '')]
        if len(s) < 2:
            print(0)
        lirun = 0
        min_mum = s[0]
        for i in s:
            min_mum = min(i, min_mum)
            lirun = max(i - min_mum, lirun)
        print(lirun)















