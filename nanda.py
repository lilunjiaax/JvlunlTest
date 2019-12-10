import time
import sys
from selenium import webdriver
from urllib.parse import quote
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq 
import requests
import lxml
from bs4 import BeautifulSoup
import random
from email.mime.text import MIMEText

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib




def get_nanda_info():

    browser = webdriver.Chrome()
    link = 'http://job.nju.edu.cn/#!/more/special_recruit'
    # soup = get_link_content(link, '南京大学')
    # info_urls = soup.select('.news-list ul')
    # print(info_urls.find_all('li'))

    browser.get(link)
    # time.sleep(80)
    browser.maximize_window()
    css_ul = '#main > div.ng-scope > div > div > div.ng-scope > div:nth-child(2) > div > div > ul > li'

    li_list = browser.find_elements_by_css_selector(css_ul)
    nanda_info_list = []
    for i in li_list:
        context = {}
        i_info = i.text.split("\n")
        context['time'] = i_info[0]
        context['address'] = i_info[1]
        context['title'] = i_info[2]
        context['detail'] = i.find_elements_by_css_selector("*")[-1].get_attribute("href")
        nanda_info_list.append(context)
    return nanda_info_list

nanda_info_list = get_nanda_info()

print(nanda_info_list)