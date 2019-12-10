import time
import os
import subprocess

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


"""
















