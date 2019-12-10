运行环境：
1. python 3.7.2
2. pandas 0.24.1

此题代码最终答案分为三个部分：
1. pro1v2.py 是解决problem1.pk问题的代码
2. pro2v2.py 是解决problem2.pk问题的代码
3. means.py 是公共的工具模块（包含读取，删除，写入）

执行：
1. python pro1v2.py problem1.pk aim_name1.pk
2. python pro2v2.py problem2.pk aim_name2.pk

其他：
1. pk文件的读取和写入路径都是代码所在的路径
2. 由于没有对div_c_t标签里面的string处理，在删除时被删掉，故产生的新文件大小与原文件相比较小
3. 代码执行过程中会有一些输出：都是统计div_cc里面包含有多少个div_c_t的结果