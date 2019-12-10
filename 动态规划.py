'''
背包问题：

'''
a_dict = {'a': [2, 6], 'b': [2, 3], 'c': [6, 5], 'd': [5, 4], 'e': [4, 6]}
a_list = ['a', 'b', 'c', 'd', 'e']
n = int(input("请输入你的背包容量: "))

# for i in reversed(list(a_dict.keys())):

def func(i, j):
    """8
    i: 前i件商品
    j: 背包存放的重量
    """
    if i == 0:
        return 0
    if j - a_dict[a_list[i-1]][0] < 0:
        return 0

    aa = max(func(i-1, j), func(i-1, j - a_dict[a_list[i-1]][0]) + a_dict[a_list[i-1]][1])
    print('--------',aa)
    return aa

# value_1 = func(len(a_list), n)

# print(value_1)


#n：物品件数；c:最大承重为c的背包；w:各个物品的重量；v:各个物品的价值
#第一步建立最大价值矩阵(横坐标表示[0,c]整数背包承重):(n+1)*(c+1)
#技巧:python 生成二维数组(数组)通常先生成列再生成行
def bag(n,c,w,p):
    res=[[-1 for j in range(c+1)]for i in range(n+1)]
    for j in range(c+1):
        #第0行全部赋值为0，物品编号从1开始.为了下面赋值方便
        res[0][j]=0
    for i in list(range(n+1))[1:]:
        for j in list(range(c+1))[1:]:
            res[i][j]=res[i-1][j]
            #生成了n*c有效矩阵，以下公式w[i-1],p[i-1]代表从第一个元素w[0],p[0]开始取。
            if(j>=w[i-1]) and res[i-1][j-w[i-1]]+p[i-1]>res[i][j]:
                res[i][j]=res[i-1][j-w[i-1]]+p[i-1]
    return res
#以下代码功能：标记出有放入背包的物品
#反过来标记，在相同价值情况下，后一件物品比前一件物品的最大价值大，则表示物品i#有被加入到背包，x数组设置为True。设初始为j=c。
def show(n,c,w,res):  
    print('最大价值为:',res[n][c])  
    x=[False for i in range(n)]  
    j=c  
    for i in range(1,n+1):  
        if res[i][j]>res[i-1][j]:  
            x[i-1]=True  
            j-=w[i-1]  
    print ('选择的物品为:')  
    for i in range(n):  
        if x[i]:  
            print ('第',i,'个,') 
    print('') 
if __name__=='__main__':  
    n=5  
    c=10  
    w=[2,2,6,5,4]  
    p=[6,3,5,4,6]  
    res=bag(n,c,w,p)  
    show(n,c,w,res) 


