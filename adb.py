import subprocess
import os
import time

"""
模拟点击位置：
import os
os.system('adb shell input tap 100 100');

实现截图判断：
import os
os.system("adb shell /system/bin/screencap -p /sdcard/4.png")
0


将截图保存到电脑：
os.system("adb pull /sdcard/4.png d:phone_file/5.png")
/sdcard/4.png: 1 file pulled. 12.3 MB/s (496759 bytes in 0.038s)
0

滑屏移动：每一个栏的像素是 ：328
>>> os.system("adb shell input swipe 200 828 200 500 1000")
                                     200 565 200 400
                                         800     635
0
每次只点击 230 600坐标，进入菜单或视频

"""


"""
点击 进入菜单 ： 点击240 500 进入目录，

点击视频播放 点击视频，点击退出 15 30 ，滑动屏幕，点击播放，点击退出


"""

a_dict = {

    0:{0:15,1:16,2:12,3:4},
    1:{0:24,1:22,2:22,3:25},
    # 0:{0:1, 1:1, 2:1, 3:1},
    # 0:{0:15, 1:16, 2:12, 3:4},
    # 1:{0:24, 1:22, 2:22, 3:25},
    # 2:{0:4, 1:3, 2:4, 3:4, 4:3, 5:4, 6:4},
    # 3:{0:3, 1:4, 2:3, 3:4, 4:4, 5:4, 6:4, 7:4, 8:4, 9:4, 10:4, 11:4, 12:4},
    # 4:{0:17,1:14,2:25,3:16,4:22,5:12},
    # 5:{0:4,1:4,2:4},
    # 6:{0:4,1:4,2:3,3:4,4:4},
    # 7:{0:4,1:4,2:4},
    # 8:{0:16,1:4,2:15,3:6,4:5,5:23,6:19,7:9,8:2},
    # 9:{0:23},
    # 10:{0:35,1:13,2:30,3:19},
    # 11:{0:22,1:20,2:33},
    # 12:{0:18,1:29,2:15,3:10,4:5},
    # 13:{0:25,1:18,2:16},
    # 14:{0:22,1:14,2:15,3:18,4:8},
    # 15:{0:33,1:26,2:22,3:13},
    # 16:{0:19,1:34,2:11,3:9,4:13},
    # 17:{0:18,1:14,2:37},
    # 18:{0:28,1:40,2:18,3:25},
    # 19:{0:26,1:23,2:15,3:20},
    # 20:{0:22,1:18,2:18,3:33},
    # 21:{0:11,1:11,2:11,3:11,4:11,5:11,6:10,7:10,8:10,9:11},
    # 22:{0:4,1:4,2:5,3:5,4:4,5:4,6:3,7:4,8:5,9:4,10:4},
    # 23:{0:4,1:4,2:4}
}
click_enter = "adb shell input tap %d %d" % (230, 600)
click_enter_last = "adb shell input tap %d %d" % (230, 800)
slip1 = "adb shell input swipe 200 800 200 635 1000"
click_mulu = "adb shell input tap %d %d" % (240, 500)
click_backup = "adb shell input tap %d %d" % (15, 30)
click_jihuo = "adb shell input tap %d %d" % (400, 200)
click_backup2 = "adb shell input tap %d %d" % (23, 75)
print("自检成功，开始执行....")
for i in a_dict:
    print("目录为：{}".format(i))
    os.system(click_enter)
    time.sleep(1)
    os.system(click_mulu)
    time.sleep(1)
    video_num = len(a_dict[i])
    for j in a_dict[i]:
        print("第 {} 个视频开始播放".format(j+1))
        if j == (video_num-1):
            print("---为最后一个视频---")
            if j == 0:
                os.system(click_enter)
            else:
                os.system(click_enter_last)
        else:
            os.system(click_enter)
        time.sleep(5)
        time.sleep(a_dict[i][j]*60)   # 
        print("第 {} 个视频播放结束".format(j+1))
        os.system(click_jihuo)
        time.sleep(1)
        os.system(click_backup)
        time.sleep(1)
        os.system(slip1)
        time.sleep(2)
        if j == (video_num-1):
            os.system(click_backup2)
            time.sleep(1)
    
    time.sleep(1)
    os.system(slip1)
    time.sleep(2)
    print("开始播放下一个目录")  

