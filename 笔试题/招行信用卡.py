

# import sys
# if __name__ == "__main__":
#     n = int(sys.stdin.readline().strip())
#     a1 = sys.stdin.readline().strip()
#     b1 = sys.stdin.readline().strip()
#     a_list = [int(i) for i in a1.split()]
#     b_list = [int(i) for i in b1.split()]
#     i = 0
#     count = 0
#     while i < n:
#         if b_list[i] <= a_list[i]:
#             count += b_list[i]
#             a_list[i] = 0
#             i = i+1
#             continue
#         if b_list[i] > a_list[i] and (a_list[i] != 0):
#             count += a_list[i]
#             b_list[i] -= a_list[i]
#             a_list[i] = 0
#
#         else:
#             if b_list[i] < a_list[i+1]:
#                 count += b_list[i]
#                 a_list[i+1] -= b_list[i]
#                 i += 1
#                 continue
#             else:
#                 count += a_list[i+1]
#                 a_list[i+1] = 0
#                 i += 1
#                 continue
#     print(count)


# import sys
# if __name__ == "__main__":
#     s1 = sys.stdin.readline().strip()
#     m, n = [int(i) for i in s1.split()]
#     a_sum = 2019
#     for i in range(m, n):
#         for j in range(i+1, n+1):
#             tmp = (i*j) % 2019
#             if tmp < a_sum:
#                 a_sum = tmp
#     print(a_sum)


import sys
def func1(a_list, i):
    if a_list[i][0] == "R":
        # 需要向右
        count = 0
        for k in a_list[i+1:]:
            count += 1
            if k[0] == "L":
                break
        if count == 1:
            # 说明是紧邻着的，位置不变
            return
        elif count > 1:
            a_list[i+count-count%2][1] += 1
            a_list[i][1] = 0

    if a_list[i][0] == "L":
        # 需要向左
        count = 0
        for k in range(i-1, 0, -1):
            count += 1
            if a_list[k][0] == "R":
                break
        if count == 1:
            return
        elif count > 1:
            a_list[i-count+count%2][1] += 1
            a_list[i][1] = 0
if __name__ == "__main__":
    s1 = sys.stdin.readline().strip()
    count_list = []
    for i in s1:
        count_list.append([i, 1])
    for i in range(len(s1)):
        func1(count_list, i)
    if not s1:
        print()
    else:
        for i in count_list:
            print(i[1], end=' ')















