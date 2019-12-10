"""
简单选择排序：依次遍历未排序的列表，选出其中的最小值，插在对应的位置
第一次遍历[0:n]得到最小值，排在第一个位置，
第二次遍历[1:n]得到最小值，排在第二个位置，
。。。。

"""
def selectionSort(a_list):
    """
    选择排序
    :param a_list:
    :return:
    """
    a_len = len(a_list)
    for i in range(a_len):
        a_min = a_list[i]
        ind = i
        for j in range(i+1, a_len):
            if a_list[j] < a_min:
                a_min = a_list[j]
                ind = j
        tmp = a_list[i]
        a_list[i] = a_list[ind]
        a_list[ind] = tmp
        
    return a_list        


def bubbleSort(a_list):
    """
    冒泡排序：从小到大
    :param a_list:
    :return:
    """
    a_len = len(a_list)
    for i in range(a_len):
        for j in range(a_len-1-i):  # 已经冒泡排序号得就不需要再比对了
            if a_list[j+1] < a_list[j]:
                a_list[j+1], a_list[j] = a_list[j], a_list[j+1]

    return a_list


def insertSortSearch(a_list):
    """
    简单插入排序
    :param a_list:
    :return:
    """
    a_len = len(a_list)
    for i in range(1, a_len):
        # 从后往前遍历之前有序得列表
        tmp = a_list[i]
        flag = 0
        for j in range(i-1, -1, -1):
            if a_list[j] > tmp:
                a_list[j+1] = a_list[j]
            else:
                a_list[j+1] = tmp
                flag = 1
                break
        if not flag:
            a_list[0] = tmp

    return a_list


################################################################################
def shellSort(a_list):
    """
    希尔排序
    :param a_list:
    :return:
    """
    a_index = 4
    a_len = len(a_list)
    for i in range(a_index, 0, -1):
        zu_num = a_len // i + 1 if a_len % i != 0 else a_len // i
        for k in range(i):
            tmp_list = []
            for j in range(zu_num):
                if i*j+k < a_len:
                    tmp_list.append(a_list[i*j + k])
            tmp_list = selectionSort(tmp_list)
            for j in range(len(tmp_list)):
                a_list[i*j + k] = tmp_list[j]
    return a_list


#################################################################################
def quickSort(a_list):
    """
    快速排序
    :param a_list:
    :return:
    """
    if not a_list:
        return []
    flag = a_list[0]
    return quickSort([i for i in a_list if i < flag]) + [i for i in a_list if i == flag] + quickSort([i for i in a_list if i > flag])


#################################################################################
def mergeSortRecursive(a_list):
    """
    归并排序，主要采用递归 + 分治的策略
    :param a_list:
    :return:
    """
    a_len = len(a_list)
    if a_len > 1:
        resu_list = []
        left = mergeSortRecursive(a_list[:a_len//2])
        right = mergeSortRecursive(a_list[a_len//2:])
        left_len = len(left)
        right_len = len(right)
        i = 0
        j = 0
        while i < left_len and j < right_len:
            if left[i] < right[j]:
                resu_list.append(left[i])
                i += 1
            else:
                resu_list.append(right[j])
                j += 1
        if i < left_len:
            resu_list.extend(left[i:])
        if j < right_len:
            resu_list.extend(right[j:])
        return resu_list
    return a_list


##################################################################################
def move_item(a_list, i):
    """
    移动堆内元素
    :param a_list:
    :param i:
    :return:
    """
    a_len = len(a_list)
    while i < a_len:
        if 2*i+1 < a_len and (2*i+2 < a_len):
            if a_list[2 * i + 1] >= a_list[2 * i + 2]:
                if a_list[i] < a_list[2 * i + 1]:
                    a_list[i], a_list[2 * i + 1] = a_list[2 * i + 1], a_list[i]
                    i = 2*i + 1
                    continue
            else:
                if a_list[i] < a_list[2 * i + 2]:
                    a_list[i], a_list[2 * i + 2] = a_list[2 * i + 2], a_list[i]
                    i = 2*i + 2
                    continue
        elif 2*i+1 < a_len:
            if a_list[i] < a_list[2 * i + 1]:
                a_list[i], a_list[2 * i + 1] = a_list[2 * i + 1], a_list[i]
                i = 2+i + 1
                continue
        break

def heapSort(a_list):
    """
    堆排序：先构建一个最大堆，
    然后将最大堆的第一个和最后元素互换位置，取出最后一个元素，
    然后调整堆顶元素，所以需要两个函数，构造最大堆函数，每次取数后的调整堆顶函数
    :param a_list:
    :return:
    """
    a_len = len(a_list)
    for i in range((a_len-1)//2, -1, -1):
        move_item(a_list, i)
    # 已经构成了最小堆
    resu_list = []
    while a_list:
        a_list[0], a_list[-1] = a_list[-1], a_list[0]
        resu_list.append(a_list[-1])
        a_list.pop(-1)
        move_item(a_list, 0)

    return resu_list[::-1]


###########################################################################
def radixSort(a_list, radix=10):
    """
    基数排序：列表中最大的数的位数，要以他为最大的基数
    基数排序在构建存储数据的容器上有点类似于桶排序
    :param a_list:
    :return:
    """
    # 对于数字的比较我们一般将基数设为10
    a_max = a_list[1]
    for i in a_list[1:]:
        if a_max < i:
            a_max = i
    K = 0
    while a_max:
        a_max = a_max // radix
        K += 1
    for i in range(1, K+1):
        bucket = [[] for j in range(radix)]
        for val in a_list:
            bucket[val%(radix**i)//(radix**(i-1))].append(val)
        del a_list[:]
        for item in bucket:
            a_list.extend(item)
    return a_list


##################################################################
def BucketSort(a_list, bucket_num=5):
    """
    桶排序
    :param a_list:
    :return:
    """
    a_len = len(a_list)
    a_max = max(a_list) + 1  # 将后边界值加1可以忽略掉最后一个桶的后边界值得包含
    a_min = min(a_list)
    a_minus = a_max - a_min
    bucket_index = a_minus / bucket_num
    bucket = [[] for i in range(bucket_num)]
    for i in range(0, bucket_num):
        # print([a_min, a_min+bucket_index])
        for j in a_list:
            if j >= a_min and (j < a_min+bucket_index):
                if not bucket[i]:
                    bucket[i].append(j)
                    continue
                tmp_len = len(bucket[i])
                bucket[i].append(j)
                for k in range(tmp_len, 0, -1):
                    if bucket[i][k] < bucket[i][k-1]:
                        bucket[i][k], bucket[i][k-1] = bucket[i][k-1], bucket[i][k]
        a_min += bucket_index
    # 合并桶
    del a_list[:]
    for i in bucket:
        a_list.extend(i)
    return a_list

#
# if __name__ == "__main__":
#     a_list = [3, 4, 1, 10, 8, 5, 9, 11, 18, 13, 101]
#     # print(selectionSort(a_list))
#     # print(bubbleSort(a_list))
#     # print(insertSortSearch(a_list))
#     # print(quickSort(a_list))
#     # print(mergeSortRecursive(a_list))
#     # print(heapSort(a_list))
#     # print(radixSort(a_list))
#     # print(BucketSort(a_list))
#     print(shellSort(a_list))






