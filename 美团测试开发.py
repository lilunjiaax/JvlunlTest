"""
删除字符
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 65536KB；其他语言 589824KB
题目描述：
将给定的字符串，按照规则删除字符，输出删除后的字符串。删除规则为：相同字符连续，则删除，如”aaaab”删除后的字符串为”b” 。注：仅是单个字符连续才删除，如babababa则不能删除；
输入
输入数据有多组，每组一行，仅包含数字和英文字母，不包含转义等其他特殊字符，输入数据最大长度为10；
输出
对于每个测试实例，要求输出按规则删除后的数据，每个测试实例的输出占一行。如果删除后有字符，直接输出删除后的字符；如果删除后为空，则输出”no”

样例输入
aaaaabbbb
样例输出
no

提示
输入样例2
a

输出样例2
a

"""


# while 1:
#     s = input().strip()
#     if s != '':
#         s1 = [i for i in s]
#         a_list = []
#         a_len = len(s1)
#         i = 0
#         while i < a_len:
#             tmp = s1[i]
#             flag = 0
#             while 1:
#                 i += 1
#                 if i < a_len:
#                     if s1[i] != tmp:
#                         break
#                     flag = 1
#                 else:
#                     flag = 1
#                     if s1[i-1] != s1[i-2]:
#                         a_list.append(tmp)
#                     break
#             if not flag:
#                 a_list.append(tmp)
#         if a_list:
#             print(''.join(a_list))
#         else:
#             print('no')
#     else:
#         break

"""


"""
while 1:
    s1 = input().strip()
    s2 = input().strip()
    if s1 != '':
        # 考虑s2为空
        if not s2:
            print(s1)
            continue
        a_list1 = [i for i in s1]
        a_list2 = [i for i in s2]

        flag = 0
        # 考虑不包含可能
        for i in a_list2:
            if i not in a_list1:
                flag = 1
                break
            elif a_list2.count(i) > a_list1.count(i):
                flag = 1
                break
        if flag:
            print('')
            continue

        index_list = []
        a_len_1 = len(a_list1)
        for i in a_list2:
            for j in range(a_len_1):
                if a_list1[j] == i:
                    if j not in index_list:
                        index_list.append(j)
                    else:
                        continue

        a, b = min(index_list), max(index_list)
        print(s1[a: b+1])
    else:
        break

