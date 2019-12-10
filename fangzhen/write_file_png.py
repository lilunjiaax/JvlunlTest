
import time
import os
from loguru import logger
import pyautogui as png
import cv2 as cv
import base64
from Common import *
from PIL import ImageGrab
from write_logging import Date_Time


class Image_Process():
    def __init__(self):
        pass

    def shoot_png(self, x1, y1, x2, y2):
        """
        传入坐标，实现精准截图
        :param x1:
        :param y1:
        :param x2:
        :param y2:
        :return: <PIL.Image.Image image mode=RGB size=100x100 at 0x20BCD1D0F98>
        """
        bbox = (x1, y1, x2, y2)
        im = ImageGrab.grab(bbox)
        return im

    def save_png(self, content, image_dir, png_name=''):
        """
        保存图片
        :param content: PIL image对象
        :param image_dir: 保存目录
        :return: 文件路径--> 存入日志
        """
        time.sleep(1)
        png_name = str(time.time()).split('.')[0]+'.png' if not png_name else png_name + '.png'
        png_dir = os.path.join(image_dir, png_name)
        content.save(png_dir)
        return png_dir

    def save_png_from_base64_to_picture(self, png_base64):
        """
        base64 --> 图片
        :param png_base64:
        :return:
        """
        png_name = os.path.join(LOGIN_IMG, str(time.time()).replace('.', '') + '.png')
        png_bytes = bytes(png_base64, encoding='utf-8')
        png_content = base64.b64decode(png_bytes)
        f = open(png_name, 'wb')
        f.write(png_content)
        f.close()
        time.sleep(2)
        print('保存的图片：'+png_name)
        pass

    def get_newest_login_file(self):
        """
        获取验证码文件夹中最新保存的验证码图片
        :return: 最新创建的图片的绝对路径
        """
        login_file_pngs = os.listdir(LOGIN_IMG)
        tmp = sorted(login_file_pngs, key=lambda item: os.path.join(LOGIN_IMG, item), reverse=True)
        print('选取的图片: '+os.path.join(LOGIN_IMG, tmp[0]))
        return os.path.join(LOGIN_IMG, tmp[0])


    def get_base64_from_png(self, image_dir):
        resu = False
        with open(image_dir, 'rb') as f:
            resu = f.read()
        return resu
            # return base64.b64decode(f.read(), '-_')

    def judge_png(self, user_name, image_root=Benchmark):
        """
        使用base64来判断图片是否一致
        :param PNG: 截取后刚保存的图片 save_png()的返回值
        :param image_root: 对比基准的图片目录
        :return: 返回仿真实验任务进度
        """
        # PNG 保存保存为临时文件(Benchmark)， 用作校验
        tmp_png_dir = os.path.join(image_root, 'tmp.png')
        tmp_bs64 = self.get_base64_from_png(tmp_png_dir)
        status_png_name = False
        tmp_list = os.listdir(image_root)
        tmp_list.remove('tmp.png')
        for png_item in tmp_list:
            if self.get_base64_from_png(os.path.join(image_root, png_item)) == tmp_bs64:
                status_png_name = png_item.replace('.png', '')
                logger.info("用户: {} , 任务进度: {}".format(user_name, status_png_name.replace(".png", '')))
                break
            else:
                continue
        if not status_png_name:
            status_png_name = str(time.time()).split('.')[0] + '.png'  # 使用时间戳命名表示图片未知
        old_png_name = tmp_png_dir
        new_png_name = os.path.join(os.path.join(os.path.join(RESOURCES_DIR, Date_Time().get_date_name()), user_name), status_png_name+'.png')
        try:
            os.rename(old_png_name, new_png_name)
        except:
            pass
        return status_png_name


# im1 = Image_Process()
#
# im1.save_png_from_base64_to_picture('')
#
# print(im1.get_newest_login_file())

# im1.judge_png('15251853026')

# b1 = im1.get_base64_from_png(os.path.join(Benchmark, 'tmp.png'))
# b2 = im1.get_base64_from_png(os.path.join(Benchmark, '用户数预测页面.png'))
#
# print(b1 == b2)























