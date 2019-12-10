'''
@Descripttion: 最多的整块个数
@Author: daxiong
@Date: 2019-08-19 15:41:02
@LastEditors: daxiong
@LastEditTime: 2019-08-19 16:02:15
'''


def maxBox(n):
    res = 0
    nsqure = n ** 2

    for i in range(1, n):
        temp = nsqure - i ** 2
        res += int(temp ** 0.5)

    return res * 4


print(maxBox(3))



'''
@Descripttion: 最大的雨水坑
@Author: daxiong
@Date: 2019-08-19 15:42:49
@LastEditors: daxiong
@LastEditTime: 2019-08-19 15:56:36
'''

def getMaxWater(array):
    left = 0
    right = len(array) - 1
    maxLeft = array[left]
    maxRight = array[right]
    maxWater = (min(maxLeft, maxRight) * (right - left))

    while left < right:
        if maxLeft <= maxRight:
            while left < right and array[left] <= maxLeft:
                left += 1
            if left == right:
                break
            else:
                maxLeft = array[left]
                if (min(maxLeft, maxRight) * (right - left)) > maxWater:
                    maxWater = (min(maxLeft, maxRight) * (right - left))
        else:
            while right > left and array[right] <= maxRight:
                right -= 1
            if left == right:
                break
            else:
                maxRight = array[right]
                if (min(maxLeft, maxRight) * (right - left)) > maxWater:
                    maxWater = (min(maxLeft, maxRight) * (right - left))
    return maxWater


array = [1, 9, 6, 2, 5, 4, 3, 10, 7]
print(getMaxWater(array))


'''
@Descripttion: 交换纸牌游戏
@Author: daxiong
@Date: 2019-08-19 15:59:14
@LastEditors: daxiong
@LastEditTime: 2019-09-01 22:29:24
'''
def change(A, B):
    sumA = sum(A)
    sumB = sum(B)
    average = int((sumA + sumB) / 2)
    res = list()

    for num in A:
        if average + num - sumA in B:
            res.append(num)
            res.append(average + num - sumA)
            break

    return res

A = [1, 3, 4]
B = [2, 2]
print(change(A, B))

