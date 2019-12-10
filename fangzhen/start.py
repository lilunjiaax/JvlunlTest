"""
驱动模块
"""

import time
import os
import shutil
import re
import threading
import queue
import winsound


from Common import *
from loguru import logger
from write_logging import Date_Time
from Init import All_Init
import pyautogui as png
import cv2 as cv
from selenium import webdriver
from before_detection import before_after_test
from process import save_picture, basis, resource_configuration_module, business_design_module, marketing_module, profit_and_loss_measurement_module, submit_file, submit_file_firefox_in_shiyanshi
from write_file_png import Image_Process


# Chrome设置忽略警告
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')

date_time = Date_Time()
day_init = All_Init(date_time.get_date_name())

# 初始化日志模块, 创建每日文件夹
day_init.Day_init()
logger.add('info.log')

# 获取任务信息
info_list = date_time.get_excel_info()

# 图片对比
IM = Image_Process()

def save_png_tmp_to_judge():
    save_picture(466, 272, 1420, 804, Benchmark, 'tmp')


def adjustment_page_chrome():
    """点击试验台"""
    png.moveTo(1811, 540, duration=1)
    png.click()
    time.sleep(20)
    # time.sleep(2)
    # png.moveTo(88, 50, duration=1)
    # png.click()
    time.sleep(20)
    png.moveTo(1811, 540, duration=1)
    png.click()


def adjustment_page_firefox():
    """点击试验台"""
    png.moveTo(1811, 540, duration=1)
    png.click()
    time.sleep(20)
    # time.sleep(2)
    # png.moveTo(88, 50, duration=1)
    # png.click()
    time.sleep(20)
    png.moveTo(1811, 540, duration=1)
    png.click()
    pass
    
def adjustment_page_firefox_with_bookmark():
    """点击试验台, firefox含标签页"""
    png.moveTo(1811, 531, duration=1)
    png.click()
    time.sleep(20)
    # time.sleep(2)
    # png.moveTo(88, 50, duration=1)
    # png.click()
    time.sleep(20)
    png.moveTo(1811, 531, duration=1)
    png.click()
def loading_re():
    """google chrome"""
    time.sleep(2)
    png.moveTo(88, -6, duration=1)
    png.click()
    time.sleep(10)
    png.moveTo(1811, 540, duration=1)
    png.click()
    time.sleep(100)


for i in info_list:
    if not i:
        logger.debug("+++++++++任务执行结束+++++++++")
        break
    number = i[3].split('.')[0]
    if not number:
        continue
    if len(str(re.findall(r'\d{11}', number)[0])) == 11:
        q = queue.Queue()
        number = re.findall(r'\d{11}', number)[0]
        # browser = webdriver.Chrome(chrome_options=option)
        browser = webdriver.Firefox()
        des_dir = day_init.Test_init(number)
        # time.sleep(10000)
        # test_code = before_after_test(browser, number)
        # 子线程执行 校验流程
        try:
            threadA = threading.Thread(target=before_after_test, args=(browser, number, q))
            threadA.start()
            threadA.join()
        except:
            pass
        test_code = -1
        if not q.empty():
            test_code = q.get()
        logger.info("用户: {} before_after_test执行完毕, test_code:{}".format(number, test_code))

        if test_code == 0:
            # todo:准备开始测试流程,注意页面接续
            adjustment_page_firefox_with_bookmark()
            start_time = time.time()
            time.sleep(300)
            while True:
                count = 1
                # 判断是否加载完成
                save_png_tmp_to_judge()
                status_name = IM.judge_png(number)
                if status_name == START_IMG:
                    logger.info("用户 {}, 试验台页面-----实验加载完成".format(number))
                    break
                if status_name == '加载失败':
                    # 刷新页面,延长等待时间，
                    time.sleep(100)
                    logger.info("用户 {}, 试验台页面-----遇到加载失败，重新刷新页面".format(number))

                logger.info("用户 {}, 试验台页面-----校验实验加载进度，第 {} 校验, 耗时总时间： {}".format(number, count, (time.time() - start_time)/60))
                time.sleep(60)
                count += 1
                if time.time() - start_time > float(3600):
                    logger.info("用户 {}, 试验台加载页面-----实验加载时间耗时{}".format(number, (time.time() - start_time)/60))
                    break
                time.sleep(100)
            if time.time() - start_time > float(3600):
                break
            basis(des_dir)
            logger.info("用户 {} 前期配置模块模块完成".format(number))
            time.sleep(30)
            resource_configuration_module(des_dir)
            logger.info("用户 {} 资源配置模块完成".format(number))
            business_design_module(des_dir)
            logger.info("用户 {} 业务设计模块完成".format(number))
            marketing_module()
            logger.info("用户 {} 市场推广模块完成".format(number))
            profit_and_loss_measurement_module(des_dir)
            logger.info("用户 {} 损益测算模块完成".format(number))
            # 提交报告
            while True:
                if time.time() - start_time > float(1800):
                    break
                time.sleep(100)

            submit_file_firefox_in_shiyanshi()
            time.sleep(30)
            save_picture(0, 0, 1900, 900, des_dir, '测试结果截图')

            time.sleep(50)
            winsound.Beep(550, 2000)
            content1 = input("请输入任意字符，驱动程序继续执行：\n")
            time.sleep(20)
            png.moveTo(1900, 10)
            png.click()

        if test_code == -1:
            # todo:三次密码重试失败,等待修正,或网页出现错误
            logger.error("用户 {} 密码所有可能尝试结束，未成功登陆".format(number))
            time.sleep(10)
            png.moveTo(1900, 10)
            png.click()
            continue
        if test_code == 1:
            time.sleep(10)
            png.moveTo(1900, 10)
            png.click()
            logger.info("用户 {} 已经测试过，结束流程".format(number))
            continue

    else:
        logger.error("手机号码验证失败 {}".format(number))
        continue








"""
#evaluate > a > div > span:nth-child(5)

"""



