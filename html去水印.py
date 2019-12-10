import os
import re
import time
shuiyin_str = "更多课程请加QQ群170701297"


from_dir = 'C:\\Users\\jvlunl\\Desktop\\html'

dest_dir = "C:\\Users\\jvlunl\\Desktop\\html去水印版"

a_list = []
os.chdir(from_dir)
for i in os.listdir():
    a_list.append(from_dir+os.sep+i)

os.chdir(dest_dir)

for i in a_list:
    f = open(i, encoding="utf8")
    a_str = f.read()
    b_str = re.sub(r'更多课程请加QQ群170701297', '', a_str)
    with open(os.path.split(i)[1], "w", encoding="utf8") as f1:
        print("开始写入{}".format(os.path.split(i)[1]))
        time.sleep(0.5)
        f1.write(b_str)

    






