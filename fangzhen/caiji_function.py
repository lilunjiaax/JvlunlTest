import pyautogui as png
import time
import os
from PIL import ImageGrab
from process import save_picture
from Common import *

#
# while True:
#     action = int(input("\n"))
#     if action == 1:
#         print("选项1：\n")
#         print(png.position())
#     if action == 2:
#         print("选项2：\n")
#         bbox = [int(i) for i in input(": \n").split(' ')]
#         print(bbox)
#         if sum(bbox) == 0:
#             # 截取全屏
#             a = png.screenshot()
#             time.sleep(1)
#             png_name = str(time.time()).split('.')[0] + '.png'
#             a.save(png_name)
#         else:
#             im = ImageGrab.grab(bbox)
#             time.sleep(1)
#             png_name = str(time.time()).split('.')[0] + '.png'
#             im.save(png_name)



# save_picture(0, 0, 200, 200, 'C:\\Users\\jvlunl\\Desktop\\test1\\仿真系统\\resources\\20191103\\15251853026', '测试装饰器的导入其他模块功能')



# time.sleep(10)
# save_picture(466, 272, 1420, 804, Benchmark, 'tmp')



