
"""
每日开始进行初始化：
1. 创建对应的文件夹 20191102
2. 


每位用户开始进行初始化：
1. 20191102 > 15251853026
2. 
"""
import time
import os
from loguru import logger
from write_logging import Date_Time
from Common import *


class All_Init():
    def __init__(self, date_dir_name):
        self.date_dir_name = date_dir_name
        self.children_dir = os.path.join(os.getcwd(), 'resources')
        self.home_dir_name = os.getcwd()
        # if 'info.log' not in os.listdir():
        #     logger.add('info.log')
        #     logger.info('------------------------')
        # logger.add('info.log')
        logger_file_list = os.listdir(LOGGER_DIR)
        if Date_Time().get_yeaterday_name() + '.log' not in logger_file_list and 'info.log' in os.listdir(HOME_DIR):
            os.rename(os.path.join(HOME_DIR, 'info.log'),
                      os.path.join(LOGGER_DIR, Date_Time().get_yeaterday_name() + '.log'))
            logger.add('info.log')
        else:
            logger.add('info.log')

    def set_logger_file(self):
        pass

    def Day_init(self):
        print("每日任务开始")
        os.chdir(self.children_dir)  # C:\Users\jvlunl\Desktop\test1\仿真系统\resources
        if self.date_dir_name not in os.listdir():
            os.mkdir(self.date_dir_name)
            logger.info("第一次进行每日初始化: {}".format(self.date_dir_name))
        else:
            logger.debug("重复进行每日初始化: {}".format(self.date_dir_name))

        os.chdir(self.home_dir_name)

    def Test_init(self, mobile_number):
        """
        返回该用户 文件夹目录
        :param mobile_number:
        :return:
        """
        os.chdir(self.children_dir)

        # todo: 按创建事件选取file_dir  直接获取实例变量
        date_dir = os.path.join(os.getcwd(), self.date_dir_name)

        os.chdir(date_dir)
        if mobile_number not in os.listdir():
            os.mkdir(mobile_number)

        User_dir = os.path.join(os.getcwd(), mobile_number)
        return User_dir



a1 = All_Init(Date_Time().get_date_name())
    











