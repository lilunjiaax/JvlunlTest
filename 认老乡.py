"""
动脑子，认老乡。
样例输入
3 1
2 3 1
5 4
1 2 1
3 4 0
2 5 1
3 2 1
"""
def fun1():
    while 1:
        s = input().strip()
        if s != '':
            n, m = [int(i) for i in s.split(" ")]
            a_list = []
            num_count = [1]
            for i in range(m):
                a_list.append([int(i) for i in input().strip().split(" ")])
            while 1:
                flag = 0
                for j in num_count[:]:
                    for i in a_list:
                        if i[2]:
                            if j == i[0]:
                                if i[1] in num_count:
                                    continue
                                else:
                                    num_count.append(i[1])

                                    flag += 1
                            if j == i[1]:
                                if i[0] in num_count:
                                    continue
                                else:
                                    num_count.append(i[0])
                                    flag += 1
                if not flag:
                    break
            print(len(num_count)-1)
        else:
            break


fun1()


"""
############## 赛码开发人员给的标准输入输出 ###################
#!/usr/bin/env python  
# coding=utf-8  
# Python使用的是3.4.3，缩进可以使用tab、4个空格或2个空格，但是只能任选其中一种，不能多种混用
import math
while 1:
    #每组第一行是N和M 
    nm = list(map(int,input().split(" ")))
    N = nm[0]
    M = nm[1]
    print(str(N) + ' ' + str(M))
    # 接下来M行，每行a b c
    for i in range(M):
      abc = list(map(int,input().split(" ")))
      a = abc[0]
      b = abc[1]
      c = abc[2]
      print(str(a) + ' ' + str(b) + ' ' + str(c))

"""