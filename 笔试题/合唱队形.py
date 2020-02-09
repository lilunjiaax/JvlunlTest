"""
题目描述：
合唱队的N名学生站成一排且从左到右编号为1到N，
其中编号为i的学生身高为Hi。现在将这些学生分成若干组（同一组的学生编号连续），
并让每组学生从左到右按身高从低到高进行排列，
使得最后所有学生同样满足从左到右身高从低到高（中间位置可以等高），那么最多能将这些学生分成多少组？

输入
第一行包含一个整数N，1≤N≤105。

第二行包含N个空格隔开的整数H1到HN，1≤Hi≤109。

输出
输出能分成的最多组数。

样例输入
4
2 1 3 2
样例输出
2

提示
补充样例
输入样例2
10
69079936 236011312 77957850 653604087 443890802 277126428 755625552 768751840 993860213 882053548
输出样例2
6

此时分组为：【69079936】【236011312 77957850】
【653604087 443890802 277126428】 【755625552】
【768751840】【 993860213 882053548】调整顺序后即可满足条件


"""
import heartrate
import sys
heartrate.trace(browser=True)
n = int(input())
s = input()
a_list = [int(i) for i in s.split(' ')]

count = 1
result0 = [a_list[0]]
for i in range(1, n):
    result0.append(a_list[i])
    a_min = min(result0)
    a_max = max(result0)
    for j in range(i+2, n):
        if a_min <= a_list[j] <= a_max:
            count += 1
            result0 = [a_list[i]]
            break

sys.stdout.write(str(count))







