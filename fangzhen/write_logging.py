from datetime import datetime, timedelta
import xlrd, xlwt
import os
import time
from Common import *
import re
class Date_Time():
    def __init__(self):
        pass

    def get_date_name(self):
        year = str(datetime.now().year)
        month = '0' + str(datetime.now().month) if len(str(datetime.now().month)) < 2 else str(datetime.now().month)
        day = '0' + str(datetime.now().day) if len(str(datetime.now().day)) < 2 else str(datetime.now().day)
        return year+month+day

    def get_yeaterday_name(self):
        yesterday = datetime.today() + timedelta(-1)
        return yesterday.strftime('%Y%m%d')

    def get_excel_info(self):
        os.chdir(HOME_DIR)
        excel_dir = os.path.join(HOME_DIR, 'tmp.xlsx')
        workbook = xlrd.open_workbook(excel_dir)
        sheet1 = workbook.sheet_by_name('Sheet1')
        info_list = []
        for i in range(2, sheet1.nrows):
            tmp = [sheet1.cell(i, 1).value, sheet1.cell(i, 2).value, sheet1.cell(i, 3).value, str(sheet1.cell(i, 4).value)]
            info_list.append(tmp)

        return info_list

    def get_number_from_dir(self, dir_name):
        dir_items = [i for i in os.listdir(dir_name) if len(re.findall(r'\d', i)) == 11 and os.path.isdir(os.path.join(dir_name, i))]
        return dir_items





















































"""
日志模块

存储模块

结构：
文件夹>每日日期文件夹>用户文件夹（手机号命名）>图片（按时间命名），日志文件

"""















