"""
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
"""
# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
# class Solution:
#     # 返回 RandomListNode
#     def Clone(self, pHead):
#         # write code here
#         p = pHead
#         # 复制
#         while p:
#             temp = p.next
#             des = RandomListNode(p.label)
#             p.next = des
#             des.next = temp
#             p = temp
#
#         # 确定随机指针
#         p = pHead
#         while p:
#             des = p.next
#             if p.random:
#                 des.random = p.random.next
#             p = des.next
#         # 进行分离操作
#         head = pHead.next
#         p = head
#         while p.next:
#             temp = p.next.next
#             p.next = temp
#             p = temp
#
#         return head

#
# class Solution:
#     # 返回 RandomListNode
#     def Clone(self, pHead):
#         # write code here
#         head = pHead
#         p_head = None
#         new_head = None
#
#         random_dic = {}
#         old_new_dic = {}
#
#         while head:
#             node = RandomListNode(head.label)
#             node.random = head.random
#             old_new_dic[id(head)] = id(node)
#             random_dic[id(node)] = node
#             head = head.next
#
#             if new_head:
#                 new_head.next = node
#                 new_head = new_head.next
#             else:
#                 new_head = node
#                 p_head = node
#
#         new_head = p_head
#         while new_head:
#             if new_head.random != None:
#                 # 在 id(1) : id(2) 和 id(2) : node 之间建立了对照关系字典
#                 new_head.random = random_dic[old_new_dic[id(new_head.random)]]
#             new_head = new_head.next
#         return p_head
#
# a = RandomListNode(1)
# b = RandomListNode(2)
# c = RandomListNode(3)
#
# a.next = b
# b.next = c
# a.random = c
#
# so = Solution()
# so.Clone(a)


"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# class Solution:
#     def __init__(self):
#         self.stack = []
#         self.middle = []
#     def push(self, item):
#         self.stack.append(item)
#     def pop(self):
#         return self.stack.pop()
#
#     def Convert(self, pRootOfTree):
#         # write code here
#         if not pRootOfTree:
#             return None
#
#         p = pRootOfTree
#         while p or self.stack:
#             while p:
#                 self.push(p)
#                 p = p.left
#             if self.stack:
#                 p = self.pop()
#                 self.middle.append(p)
#                 p = p.right
#         for i in range(len(self.middle)-1):
#             self.middle[i].right = self.middle[i+1]
#             self.middle[i+1].left = self.middle[i]
#         return self.middle[0]
#
# root = TreeNode(5)
# four = TreeNode(4)
# three = TreeNode(3)
# seven = TreeNode(7)
# root.left = four
# root.right = seven
#
# four.left = three
#
# so = Solution()
# so.Convert(root)

"""
题目描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
"""
"""
这一类问题一般可以概括为树形问题：

"""
# -*- coding:utf-8 -*-
# class Solution:
#     def Permutation(self, ss):
#         # write code here
#         if not ss:
#             return []
#         res = []
#         self.digui(ss, res, '')
#         return sorted(list(set(res)))
#
#     def digui(self, ss, res, path):
#         if not ss:
#             res.append(path)
#         else:
#             for i in range(len(ss)):
#                 self.digui(ss[:i]+ss[i+1:], res, path+ss[i])
#
#
#
# so = Solution()
# so.Permutation('abc')


"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，
超过数组长度的一半，因此输出2。如果不存在则输出0。
"""

# -*- coding:utf-8 -*-
# class Solution:
#     def MoreThanHalfNum_Solution(self, numbers):
#         # write code here
#         '''
#         进行排序
#         :param numbers:
#         :return:
#         '''
#         numbers.sort()
#         count = len(numbers)
#         des = numbers[count // 2]
#         cou = numbers.count(des)
#         if cou > count//2:
#
#             return numbers[count // 2]
#         else:
#             return 0
#
# so = Solution()
# print(so.MoreThanHalfNum_Solution([1, 2, 3, 2, 2, 2, 5, 4, 2]))

"""
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
"""
# -*- coding:utf-8 -*-
# class Solution:
#     def GetLeastNumbers_Solution(self, tinput, k):
#         # write code here
#         if k>len(tinput):
#             return []
#         tinput.sort()
#         return tinput[0:k]


"""
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。
今天测试组开完会后,
他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,
当向量全为正数的时候,问题很好解决。
但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？
例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)
"""

# -*- coding:utf-8 -*-
# class Solution:
#     def FindGreatestSumOfSubArray(self, array):
#         # write code here
#         a_count = len(array)
#         a_dict = {}
#         b_dict = {}
#         i = 0
#         while i< a_count:
#             if array[i] > 0:
#                 # 求正串的和
#                 sum1, id1 = self.get_sum(array, i, 1)
#                 a_dict[id1-1] = sum1
#                 i = id1
#                 continue
#             if array[i] < 0:
#                 sum1, id1 = self.get_sum(array, i, 0)
#                 a_dict[id1-1] = sum1
#                 i = id1
#                 continue
#             if array[i] == 0:
#                 i = i+1
#                 continue
#
#
#     def get_sum(self, array, i, flag):
#         if flag == 1:
#             # 求正串的和
#             res = []
#             for j in range(i, len(array)):
#                 if array[j] < 0:
#                     break
#                 res.append(array[j])
#             return sum(res), j
#         elif flag == 0:
#             # 求负串的和
#             res = []
#             for j in range(i, len(array)):
#                 if array[j] > 0:
#                     break
#                 res.append(array[j])
#             return sum(res), j

# class Solution:
#     def FindGreatestSumOfSubArray(self, array):
#         maxsum, maxhere = array[0], array[0]
#         for i in array[1:]:
#             if maxhere <= 0:
#                 maxhere = i
#             else:
#                 maxhere += i
#             if maxhere > maxsum:
#                 maxsum = maxhere
#         return maxsum
#
#
# so = Solution()
# so.FindGreatestSumOfSubArray([6, -3, -2, 7, -15, 1, 2, 2])


"""
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
"""


# -*- coding:utf-8 -*-
# class Solution:
#     def NumberOf1Between1AndN_Solution(self, n):
#         # write code here
#         a_str = ''
#         for i in range(1, n + 1):
#             a_str += str(i)
#         return a_str.count('1')

"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
"""

# -*- coding:utf-8 -*-
# class Solution:
#     def PrintMinNumber(self, numbers):
#         if not numbers:
#             return ''
#         # write code here
#         numbers = [str(i) for i in numbers]
#         numbers = self.Permutation(numbers)
#         numbers = [int(i) for i in numbers]
#         return min(numbers)
#
#     def Permutation(self, ss):
#         # write code here
#         if not ss:
#             return []
#         res = []
#         self.digui(ss, res, '')
#         return sorted(list(set(res)))
#
#     def digui(self, ss, res, path):
#         if not ss:
#             res.append(path)
#         else:
#             for i in range(len(ss)):
#                 self.digui(ss[:i]+ss[i+1:], res, path+ss[i])

"""
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，
因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

前20个丑数为：1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27, 30, 32, 36
2 3 5

"""
# -*- coding:utf-8 -*-
# class Solution:
#     def GetUglyNumber_Solution(self, index):
#         # write code here
#         if index == 1:
#             return 1
#         if index == 2:
#             return 2
#         a_list = [1, 2]
#         num = 2
#         while 1:
#             num += 1
#             if self.judge(num):
#                 a_list.append(num)
#             else:
#                 continue
#             if len(a_list) == index:
#                 break
#         return a_list[index-1]
#
#     def judge(self, num):
#         """
#         判断是不是丑数
#         :param num:
#         :return:
#         """
#         resu_list = []
#         for i in range(2, num+1):
#             if num % i == 0:
#                 if num//i not in resu_list:
#                     resu_list.append(num//i)
#                 if i not in resu_list:
#                     resu_list.append(i)
#         resu_list = list(set(resu_list))
#         resu_list.pop(resu_list.index(1))
#         if not resu_list:
#             return False
#         judge_list = [2, 3, 5]
#         for i in resu_list:
#             if self.judge2(i):
#                 if not (i in judge_list):
#                     return False
#         return True
#
#     def judge2(self, num):
#         """
#         判断是不是质数
#         :param num:
#         :return:
#         """
#         resu_list = [1, num]
#         a_list = []
#         for i in range(1, num+1):
#             if num%i == 0:
#                 a_list.append(i)
#                 a_list.append(num//i)
#         for i in a_list:
#             if not (i in resu_list):
#                 return False
#         return True
#
# so = Solution()
# print(so.GetUglyNumber_Solution(1))

"""
p = 2^x + 3^y + 5^z
1


"""
#
# class Solution:
#     def GetUglyNumber_Solution(self, index):
#         if (index <= 0):
#             return 0
#         uglyList = [1]
#         indexTwo = 0
#         indexThree = 0
#         indexFive = 0
#         for i in range(index-1):
#             newUgly = min(uglyList[indexTwo]*2, uglyList[indexThree]*3, uglyList[indexFive]*5)
#             uglyList.append(newUgly)
#             if (newUgly % 2 == 0):
#                 indexTwo += 1
#             if (newUgly % 3 == 0):
#                 indexThree += 1
#             if (newUgly % 5 == 0):
#                 indexFive += 1
#         return uglyList[-1]
#
# so = Solution()
# so.GetUglyNumber_Solution(10)


"""
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,
并返回它的位置, 如果没有则返回 -1（需要区分大小写）
"""
# -*- coding:utf-8 -*-
# class Solution:
#     def FirstNotRepeatingChar(self, s):
#         # write code here
#         a = {}
#         s1 = set(s)
#         for i in s1:
#             a[i] = 0
#         for i in s:
#             a[i] += 1
#         # 注意：当列表转化为集合时，会导致顺序混乱，所以需要按照原来的顺序遍历
#         for i in s:
#             if a[i] == 1:
#                 return s.index(i)
#         return -1
#
# so = Solution()
# print(so.FirstNotRepeatingChar('google'))

"""
逆序对：

"""
# -*- coding:utf-8 -*-
# class Solution:
#     def InversePairs(self, data):
#         # write code here
#         a_len = len(data)
#         count = 0
#         for i in range(a_len):
#             for j in range(i+1, a_len):
#                 if data[i] > data[j]:
#                     count += 1
#
#         return count % 1000000007


'''
输入两个链表，找出它们的第一个公共结点
'''

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class Solution:
#     def FindFirstCommonNode(self, pHead1, pHead2):
#         # write code here
#         p1 = pHead1
#         a1 = {}
#         while p1:
#             a1[id(p1)] = p1
#             p1 = p1.next
#
#         p2 = pHead2
#         a2 = {}
#         while p2:
#             a2[id(p2)] = p2
#             p2 = p2.next
#         for i in a1:
#             if i in a2:
#                 return a1[i]
#
# a1 = ListNode(0)
# a = ListNode(1)
# b = ListNode(2)
# c = ListNode(3)
# d = ListNode(5)
#
# a1.next = a
# a.next = d
#
# b.next = c
# c.next = d
#
# so = Solution()
# print(so.FindFirstCommonNode(a1, b).val)

"""
统计一个数字在排序数组中出现的次数
"""
# -*- coding:utf-8 -*-
# class Solution:
#     def GetNumberOfK(self, data, k):
#         # write code here
#         count = 0
#         for i in data:
#             if i==k:
#                 count+=1
#         return count


"""
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class Solution:
#     def __init__(self):
#         self._length = 1
#     def TreeDepth(self, pRoot):
#         # write code here
#         if not pRoot:
#             return 0
#         root = pRoot
#         self.digui(root, 1)
#         return self._length
#
#     def digui(self, root, length):
#         if root.left:
#             if self._length < length+1:
#                 self._length = length + 1
#             self.digui(root.left, length+1)
#         if root.right:
#             if self._length < length + 1:
#                 self._length = length + 1
#             self.digui(root.right, length+1)
#
#
# a = TreeNode(1)
# a1 = TreeNode(2)
# a2 = TreeNode(3)
# a3 = TreeNode(4)
# a4 = TreeNode(5)
# a5 = TreeNode(6)
# a6 = TreeNode(7)
#
# a.left = a1
# a.right = a2
#
# a1.left = a3
# a1.right = a4
#
# a2.right = a5
#
# a4.left = a6
#
# so = Solution()
# so.TreeDepth(a)

"""
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class Solution:
#       """
#       利用后序遍历实现判断平衡二叉树
#       """
#     def __init__(self):
#         self.stack = []
#
#     def IsBalanced_Solution(self, pRoot):
#         # write code here
#         pCur = pRoot
#         pLastNode = None
#         while pCur:
#             self.stack.append(pCur)
#             pCur = pCur.left
#         left = 0
#         right = 0
#         while self.stack:
#             pCur = self.stack.pop()
#             if (pCur.right == None) or (pLastNode == pCur.right):
#                 # 访问此根节点，顺便比较左右子树的高度
#                 if abs(left-right) > 1:
#                     return False
#                 pLastNode = pCur
#             else:
#                 self.stack.append(pCur)
#                 pCur = pCur.right
#                 while pCur:
#                     self.stack.append(pCur)
#                     pCur = pCur.left



# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class Solution:
#     """
#     利用递归求树的高度来判断平衡二叉树
#     """
#     def __init__(self):
#         self._length = 1
#
#     def TreeDepth(self, pRoot):
#         # write code here
#         self._length = 1
#         if not pRoot:
#             return 0
#         root = pRoot
#         self.digui(root, 1)
#         return self._length
#
#     def digui(self, root, length):
#         if root.left:
#             if self._length < length+1:
#                 self._length = length + 1
#             self.digui(root.left, length+1)
#         if root.right:
#             if self._length < length + 1:
#                 self._length = length + 1
#             self.digui(root.right, length+1)
#
#     def IsBalanced_Solution(self, pRoot):
#         # write code here
#         if not pRoot:
#             return True
#         if abs(self.TreeDepth(pRoot.left) - self.TreeDepth(pRoot.right)) > 1:
#             return False
#         return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)


"""
一个整型数组里除了两个数字之外，其他的数字都出现了两次。
请写程序找出这两个只出现一次的数字。
"""
# -*- coding:utf-8 -*-
# class Solution:
#     # 返回[a,b] 其中ab是出现一次的两个数字
#     def FindNumsAppearOnce(self, array):
#         # write code here
#         array = [i for i in array if array.count(i) == 1]
#         return array
# so = Solution()
# print(so.FindNumsAppearOnce([1,2,3,5,2,3,5,8]))

"""
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,
你能不能也很快的找出所有和为S的连续正数序列? Good Luck!

输出描述:
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
"""

# -*- coding:utf-8 -*-
# class Solution:
#     def FindContinuousSequence(self, tsum):
#         # write code here
#         a_list = []
#         for i in range(1, tsum):
#             resu = self.FindList(i, tsum)
#             if resu:
#                 a_list.append(resu)
#         return a_list
#
#     def FindList(self, i, tsum):
#         a_list = [i]
#         while 1:
#             i = i+1
#             a_list.append(i)
#             if sum(a_list) >= tsum:
#                 break
#         if sum(a_list) == tsum:
#             return a_list
#         return None
#
# so = Solution()
# print(so.FindContinuousSequence(1))


"""
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
输出描述:
对应每个测试案例，输出两个数，小的先输出。
"""
# -*- coding:utf-8 -*-
# class Solution:
#     def FindNumbersWithSum(self, array, tsum):
#         # write code here
#         a_list = []
#         for i in array[:]:
#             if tsum - i in array:
#                 a_list.append([i, tsum-i])
#                 array.pop(array.index(i))
#                 array.pop(array.index(tsum-i))
#         if len(a_list) >= 1:
#             b_list = a_list[0]
#             temp = b_list[0]*b_list[1]
#
#             for i in a_list[1:]:
#                 if i[0]*i[1] < temp:
#                     b_list = i
#                     temp = i[0]*i[1]
#             b_list.sort()
#             return b_list[0], b_list[1]
#         else:
#             return []

#
#
# so = Solution()
# print(so.FindNumbersWithSum([1,2,4,7,11,15],15))


"""
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
"""
# -*- coding:utf-8 -*-
# class Solution:
#     def LeftRotateString(self, s, n):
#         # write code here
#         return s[n:] + s[:n]
#
# so = Solution()
# print(so.LeftRotateString("abcXYZdef", 3))


"""
牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。
同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。
例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。
Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？
"""

# -*- coding:utf-8 -*-
# class Solution:
#     def ReverseSentence(self, s):
#         # write code here
#         s = s.split(' ')
#         s.reverse()
#         return ' '.join(s)
#
# so = Solution()
# print(so.ReverseSentence('student. a am I'))

"""
题目描述
LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...
他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！
“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,
他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。
上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。
LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何， 
如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0
"""
# -*- coding:utf-8 -*-
import collections
# class Solution:
#     def IsContinuous(self, numbers):
#         # write code here
#         if not numbers:
#             return False
#         a_list = [i for i in numbers if i > 0]
#         a_list.sort()
#         a_len = len(a_list)
#         n = 0
#         for i in range(a_len-1):
#             if a_list[i+1] - a_list[i] > 0:
#                 n += a_list[i+1] - a_list[i]
#             else:
#                 return False
#         if n > 4:
#             return False
#         else:
#             return True


"""
题目描述
每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。
HF作为牛客的资深元老,自然也准备了一些小游戏。
其中,有个游戏是这样的:
首先,让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。每次喊到m-1的那个小朋友要出列唱首歌,
然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,
从他的下一个小朋友开始,继续0...m-1报数....这样下去....直到剩下最后一个小朋友,可以不用表演,
并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。
请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)

如果没有小朋友，请返回-1
"""

# -*- coding:utf-8 -*-
# class Solution:
#     def LastRemaining_Solution(self, n, m):
#         # write code here
#         if n == 0:
#             return -1
#         a_list = list(range(n))
#         a_mod = 0
#         while a_list:
#             a_len = len(a_list)
#             if a_len == 1:
#                 temp = a_list[0]
#                 break
#             a_mod = ((m-1) % a_len + a_mod)%a_len
#             a_list.pop(a_mod)
#         return temp
#
#
#
# so = Solution()
# print(so.LastRemaining_Solution(5, 2))

"""
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
"""
# -*- coding:utf-8 -*-
# class Solution:
#     def Sum_Solution(self, n):
#         # write code here
#         if n==0:
#             return 0
#         return self.Sum_Solution(n-1) + n
#
# so = Solution()
# print(so.Sum_Solution(5))

"""
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
"""
# -*- coding:utf-8 -*-
# class Solution:
#     def Add(self, num1, num2):
#         # write code here
#         a = []
#         a.append(num1)
#         a.append(num2)
#         return sum(a)


"""
题目描述
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，
要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
输入描述:
输入一个字符串,包括数字字母符号,可以为空
输出描述:
如果是合法的数值表达则返回该数字，否则返回0

输入
+2147483647
    1a33
    
输出

2147483647
    0
"""
# -*- coding:utf-8 -*-
# class Solution:
#     def StrToInt(self, s):
#         # write code here
#         if not s:
#             return 0
#         a_list = []
#         judge = ['+', '-', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#         for i in s:
#             if i not in judge:
#                 return 0
#             a_list.append(i)
#         flag = 0
#         if a_list[0] in ['+', '-']:
#             flag = a_list[0]
#             a_list = a_list[1:]
#         num = 0
#         for i in a_list:
#             num = num*10 + int(i)
#
#         if flag == '-':
#             return -num
#         else:
#             return num
#
#
# so = Solution()
# print(so.StrToInt('0'))

"""
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 
数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
"""
# -*- coding:utf-8 -*-
# class Solution:
#     # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
#     # 函数返回True/False
#     def duplicate(self, numbers, duplication):
#         # write code here
#         a_list = []
#         for i in numbers:
#             if i in a_list:
#                 duplication[0] = i
#                 return True
#                 break
#             a_list.append(i)
#         return False
#
# so = Solution()
# kk = []
# print(so.duplicate([2,1,3,0,4], kk))
# print(kk)

"""
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法
"""
# -*- coding:utf-8 -*-
# class Solution:
#     def multiply(self, A):
#         # write code here
#         B = []
#         for i in range(len(A)):
#             B.append(self.muti(A, i))
#         return B
#
#     def muti(self, A, i):
#         num = 1
#         for j in range(len(A)):
#             if j == i:
#                 continue
#             num *= A[j]
#         return num


"""
请实现一个函数用来匹配包括'.'和'*'的正则表达式。
模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。 
在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
"""
# -*- coding:utf-8 -*-
# class Solution:
#     # s, pattern都是字符串
#     def match(self, s, pattern):
#         s = [i for i in s]
#         pattern = [i for i in pattern]
#         length = len(pattern)
#         i = 0
#         flag = 0
#         flag1 = 0
#         while i < length:
#             if i < length-1:
#                 flag += 1
#                 if pattern[i] != '.' and pattern[i] != '*' and pattern[i + 1] == '*':
#                     # a*
#                     if (not s) and (i == length-2):
#                         return True
#                     if not s:
#                         break
#                     if pattern[i] == s[0]:
#                         s.pop(0)
#                         continue
#                     else:
#                         # a*   b
#                         i += 2
#                         continue
#             if i < length - 1:
#                 flag += 1
#                 if pattern[i] == '.' and pattern[i+1] == '*':
#                     if s:
#                         temp = s[0]
#                         while s[0] == temp:
#                             s.pop(0)
#                             if not s:
#                                 break
#                     i += 2
#             if s:
#                 flag += 1
#                 if i == length:
#                     break
#                 if pattern[i] == s[0]:
#                     if s:
#                         s.pop(0)
#                         i += 1
#                     continue
#             if i < length:
#                 if pattern[i] == '.':
#                     if s:
#                         flag += 1
#                         s.pop(0)
#                         i += 1
#             if flag == flag1:
#                 break
#             flag1 = flag
#
#         if i == length and (not s):
#             return True
#         else:
#             return False
# so = Solution()
# print(so.match("aaa", "ab*ac*a"))

"""
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
"""

# -*- coding:utf-8 -*-
# class Solution:
#     # s字符串
#     def isNumeric(self, s):
#         # write code here
#         a_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#         if 'e' in s or 'E' in s:
#             if 'e' in s:
#                 left, right = s.split('e')
#             if 'E' in s:
#                 if isinstance(s, list):
#                     return False
#                 left, right = s.split('E')
#             if left == '' or right == '':
#                 return False
#             if left[0] == '+' or left[0] == '-':
#                 left = left[1:]
#             if right[0] == '+' or right[0] == '-':
#                 right = right[1:]
#             if '.' in left:
#                 left = left.split('.')
#                 if len(left) > 2:
#                     return False
#                 left = ''.join(left)
#             if '.' in right:
#                 return False
#             for i in left:
#                 if i not in a_list:
#                     return False
#             for i in right:
#                 if i not in a_list:
#                     return False
#         else:
#             s = s.split('.')
#             if len(s) > 2:
#                 return False
#             s = ''.join(s)
#             if s[0] == '+' or s[0] == '-':
#                 s = s[1:]
#             for i in s:
#                 if i not in a_list:
#                     return False
#
#         return True
# so = Solution()
# print(so.isNumeric("12e"))


"""
题目描述
请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"go"时，
第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。

输出描述:
如果当前字符流没有存在出现一次的字符，返回#字符。
"""

# -*- coding:utf-8 -*-
# class Solution:
#     # 返回对应char
#     def __init__(self):
#         self.s=''
#         self.dict1={}
#
#     def FirstAppearingOnce(self):
#         # write code here
#         for i in self.s:
#             if self.dict1[i]==1:
#                 return i
#         return '#'
#
#     def Insert(self, char):
#         # write code here
#         self.s=self.s+char
#         if char in self.dict1:
#             self.dict1[char]=self.dict1[char]+1
#         else:
#             self.dict1[char]=1


"""
题目描述
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
"""
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class Solution:
#     def EntryNodeOfLoop(self, pHead):
#         # write code here
#         p1 = pHead
#         p2 = pHead
#         while p2:
#             p1 = p1.next
#             p2 = p2.next
#             if not p2:
#                 break
#             p2 = p2.next
#             if p1 == p2:
#                 # 该链表有环
#                 return self.find_node(pHead, p1)
#
#         return None
#     def find_node(self, pHead, p):
#         a_list = []
#         while p:
#             if p in a_list:
#                 break
#             a_list.append(p)
#             p = p.next
#         while pHead:
#             if pHead in a_list:
#                 return pHead
#             pHead = pHead.next
#
#
# p1 = ListNode(1)
# p2 = ListNode(2)
# p3 = ListNode(3)
# p4 = ListNode(4)
# p5 = ListNode(5)
# p6 = ListNode(6)
# p7 = ListNode(7)
# p8 = ListNode(8)
#
# p1.next = p2
# p2.next = p3
# p3.next = p4
# p4.next = p5
# p5.next = p6
# p6.next = p7
# p7.next = p8
# p8.next = p3
#
# so = Solution()
# node = so.EntryNodeOfLoop(p1)
# print(node.val)


"""
题目描述
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

{1,1,1,1,1,1,1}
"""

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# class Solution:
#     def deleteDuplication(self, pHead):
#         # write code here
#         a_list = []
#         while pHead:
#             ne = pHead
#             flag = 0
#             if not pHead.next:
#                 a_list.append(pHead)
#                 break
#             while True:
#                 ne = ne.next
#                 if ne:
#                     if ne.val == pHead.val:
#                         flag = 1
#                         continue
#                     else:
#                         if flag == 0:
#                             a_list.append(pHead)
#                         pHead = ne
#                         break
#                 else:
#                     pHead = ne
#                     break
#         if not a_list:
#             return None
#         phead = a_list[0]
#         root = phead
#         for i in a_list[1:]:
#             phead.next = i
#             phead = phead.next
#         phead.next = None
#         return root
#
#
# p1 = ListNode(1)
# p2 = ListNode(1)
# p3 = ListNode(1)
# p4 = ListNode(1)
# p5 = ListNode(1)
# p6 = ListNode(1)
# p7 = ListNode(1)
#
#
# p1.next = p2
# p2.next = p3
# p3.next = p4
# p4.next = p5
# p5.next = p6
# p6.next = p7
#
#
# so = Solution()
# so.deleteDuplication(p1)


"""
题目描述
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。


将此结点在树中的位置分成几类来考虑，
1. 有右孩子的结点，下次遍历肯定是右子树的左...
2. 没有右孩子了，说明是叶子结点，要看是左叶子还是右叶子
2.1 左叶子 输出父节点即可
2.2 右叶子，一直向上回溯（注意边界条件）
"""
# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
# class Solution:
#     def GetNext(self, pNode):
#         # write code here
#         if pNode.right:
#             pNode = pNode.right
#             while pNode.left:
#                 pNode = pNode.left
#             return pNode
#         # 然后开始没有右孩子的情况
#         if pNode.next:
#             while pNode.next:
#                 tmp = pNode.next
#                 if tmp.left == pNode:
#                     return tmp
#                 pNode = tmp
#
#         return None

"""
题目描述
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

注意点：
二叉树的镜像翻转会导致内存里面给的那个二叉树变了，所以需要提前复制一份
然后再递归进行比较，（在递归比较时，需要注意结束条件）
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class Solution:
#     def isSymmetrical(self, pRoot):
#         # write code here
#         if not pRoot:
#             return True
#         phead = self.muti(pRoot)
#         self.Mirror(pRoot)
#         if self.digui_judge(pRoot, phead):
#             return True
#         return False
#     def digui_judge(self, p1, p2):
#         if not p1 and not p2:
#             return True
#         if not p1 or not p2:
#             return False
#         return (p1.val == p2.val) and self.digui_judge(p1.left, p2.left) and self.digui_judge(p1.right, p2.right)
#     def muti(self, pRoot):
#         if pRoot:
#             tmp1 = TreeNode(pRoot.val)
#             self.digui_make(pRoot, tmp1)
#         return tmp1
#     def digui_make(self, pRoot, temp):
#         if pRoot.left:
#             tmp = TreeNode(pRoot.left.val)
#
#             temp.left = tmp
#             self.digui_make(pRoot.left, temp.left)
#         if pRoot.right:
#             tmp = TreeNode(pRoot.right.val)
#
#             temp.right = tmp
#             self.digui_make(pRoot.right, temp.right)
#
#     def Mirror(self, root):
#         # write code here
#         self.digui(root)
#         return root
#     def digui(self, root):
#         if root:
#             root.left, root.right = root.right, root.left
#             self.digui(root.left)
#             self.digui(root.right)
#
#
# p1=TreeNode(8)
# p2=TreeNode(6)
# p3=TreeNode(9)
# p4=TreeNode(5)
# p5=TreeNode(7)
# p6=TreeNode(7)
# p7=TreeNode(5)
#
# p1.left = p2
# p1.right = p3
#
# p2.left = p4
# p2.right = p5
#
# p3.left = p6
# p3.right = p7
#
# so = Solution()
# print(so.isSymmetrical(p1))

"""
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class Solution:
#     def __init__(self):
#         self.stack1 = []
#         self.result = {}
#     def Print(self, pRoot):
#         # write code here
#         if not pRoot:
#             return []
#         pRoot.line = 0
#         self.stack1.append(pRoot)
#
#         while self.stack1:
#             tmp = self.stack1.pop(0)
#             if tmp.line in self.result:
#                 self.result[tmp.line].append(tmp.val)
#             else:
#                 self.result[tmp.line] = [tmp.val]
#             if tmp.left:
#                 tmp.left.line = tmp.line+1
#                 self.stack1.append(tmp.left)
#             if tmp.right:
#                 tmp.right.line = tmp.line + 1
#                 self.stack1.append(tmp.right)
#         a_list = []
#         for i in self.result:
#             if i % 2 == 0:
#                 a_list.append(self.result[i])
#             else:
#                 a_list.append(self.result[i][-1::-1])
#         return a_list
#
# p1=TreeNode(1)
# p2=TreeNode(2)
# p3=TreeNode(3)
# p4=TreeNode(4)
# p5=TreeNode(5)
# p6=TreeNode(6)
# p7=TreeNode(7)
# p8=TreeNode(8)
#
# p1.left = p2
# p1.right = p3
#
# p2.left = p4
# p2.right = p5
#
# p3.left = p6
# p3.right = p7
#
# p4.left = p8
#
# so = Solution()
# print(so.Print(p1))



"""
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class Solution:
#     # 返回二维列表[[1,2],[4,5]]
#     def __init__(self):
#         self.stack = []
#         self.result = {}
#     def Print(self, pRoot):
#         # write code here
#         if not pRoot:
#             return []
#         pRoot.line = 0
#         self.stack.append(pRoot)
#         while self.stack:
#             tmp = self.stack.pop(0)
#             if tmp.line in self.result:
#                 self.result[tmp.line].append(tmp.val)
#             else:
#                 self.result[tmp.line] = [tmp.val]
#             if tmp.left:
#                 tmp.left.line = tmp.line+1
#                 self.stack.append(tmp.left)
#             if tmp.right:
#                 tmp.right.line = tmp.line+1
#                 self.stack.append(tmp.right)
#
#         a_list = []
#         for i in self.result:
#             a_list.append(self.result[i])
#         return a_list
#
#
# p1=TreeNode(1)
# p2=TreeNode(2)
# p3=TreeNode(3)
# p4=TreeNode(4)
# p5=TreeNode(5)
# p6=TreeNode(6)
# p7=TreeNode(7)
# p8=TreeNode(8)
#
# p1.left = p2
# p1.right = p3
#
# p2.left = p4
# p2.right = p5
#
# p3.left = p6
# p3.right = p7
#
# p4.left = p8
#
# so = Solution()
# print(so.Print(p1))

"""
请实现两个函数，分别用来序列化和反序列化二叉树

二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，
从而使得内存中建立起来的二叉树可以持久保存。
序列化可以基于先序、中序、后序、层序的二叉树遍历方式来进行修改，
序列化的结果是一个字符串，序列化时通过 某种符号表示空节点（#），以 ！ 表示一个结点值的结束（value!）。

二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。
"""
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        # 采用层序遍历
        pass

    def Deserialize(self, s):
        # write code here
        pass





















