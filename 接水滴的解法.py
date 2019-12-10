"""
题目描述：
给定n个非负整数，表示每个宽度为1的柱子的高度图，计算按此排列的柱子，
下雨之后能接多少的雨水

输入：[0,1,0,2,1,0,1,3,2,1,2,1]

输出：6

"""

# 先使用暴力解法，对于当前所处索引的i，找到两边的最大值，然后对两个值取较小值，
# 然后和减去自己的高度且>0即可得到

a_list = [0,1,0,2,1,0,1,3,2,1,2,1]
a_len = len(a_list)

def L_max(i, a_list):
    if i == 0:
    return 
    return max(a_list[])
    
    
def R_max(i, a_len, a_list):
    pass
    


a_sum = 0
for i in range(a_len):
    temp = min(L_max(i, a_list), R_max(i, a_len, a_list)) - a_list[i]
    if  temp> 0:
        a_sum += temp


print(a_sum)
        