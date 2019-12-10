from selenium import webdriver
import os

import time

"""
1. 打开网易有钱网址
https://qian.163.com/pc/index.html#/bill/billlist

2. 调整起始时间


"""


broswer = webdriver.Chrome()

broswer.get("https://qian.163.com/pc/index.html#/bill/billlist")

time.sleep(10)

