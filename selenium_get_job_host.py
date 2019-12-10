from flask import Flask
app = Flask(__name__)


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


"""
1. 南京农业大学，南京工业大学，东南大学

2. 南京大学

3. 南京邮电大学

"""


def get_link_content(link, school_name):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }
    response = requests.get(link, headers=headers, verify=False, timeout=10) 
    time.sleep(random.randint(0, 3))
    print(school_name, 'status_code:', response.status_code)
    html_text = response.text
    soup = BeautifulSoup(html_text, 'lxml')
    return soup
  

def format_HTML(tmp, dict_list, school_name):
    tmp += '<h2>{}</h2><table><tbody>'.format(school_name)
    for i in dict_list:
        tmp += """<tr>
        <td>{}</td>
        <td>{}</td>
        <td>{}</td>
        <td><a href="{}">点击链接查看详情</a></td>
        </tr>""".format(i['title'], i['time'], i['address'], i['detail'])
    tmp+= "</tbody></table>"
    return tmp
  

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_emails(tmp, addr_email):
    from_addr = 'jvlunl@163.com'           # input('From: ')
    password = '1234qwerasdf'                         # input('Password: ')
    to_addr = addr_email                     #input('To: ')
    smtp_server = 'smtp.163.com'            # input('SMTP server: ')

    msg = MIMEText(tmp, 'html', 'utf-8')
    msg['From'] = _format_addr('宣讲会每日信息 <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('李伦佳每日问候……', 'utf-8').encode()
    
    server = smtplib.SMTP_SSL(smtp_server)
    # server.set_debuglevel(1)

    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()



@app.route('/')
def hello_world():

    # 东南大学
    link = 'http://seu.91job.org.cn/teachin'
    soup = get_link_content(link, "东南大学")
    info_urls = soup.find_all('ul', class_='infoList teachinList')
    dongnan_info_list = []
    # title, address, time, detail
    for item_info in info_urls:
        lis = item_info.find_all("li")
        context = {}
        context['title'] = lis[0].a.string
        context['address'] = lis[2].string + '    '+ lis[3].string
        context['time'] = lis[4].string
        context['detail'] = 'http://seu.91job.org.cn'+ lis[0].a.attrs['href']
        dongnan_info_list.append(context)

  

    # 南京工业大学
    link = 'http://njtech.91job.org.cn/'
    soup = get_link_content(link, '南京工业大学')
    info_urls = soup.find_all(attrs={'id': 'tabs-d'})
    lis_list = info_urls[0].find_all('li')
    
    gongye_info_list = []
    for items in lis_list:
        context = {}
        aTag_s = items.find_all("a")
        context['title'] = aTag_s[1].string
        context['time'] = items.span.string
        context['address'] = aTag_s[0].string
        context['detail'] = link[:-1] + aTag_s[1].attrs['href']
        gongye_info_list.append(context)
    # print(gongye_info_list)


    # 南京农业大学
    
    link = 'http://njau.91job.org.cn/'
    soup = get_link_content(link, '南京农业大学')
    info_urls = soup.find_all(attrs={'id': 'tabs-23'})
    lis_list = info_urls[0].find_all('li')
    
    nongye_info_list = []
    for items in lis_list:
        context = {}
        aTag_s = items.find_all("a")
        context['title'] = aTag_s[1].string
        context['time'] = items.span.string
        context['address'] = aTag_s[0].string
        context['detail'] = link[:-1] + aTag_s[1].attrs['href']
        nongye_info_list.append(context)


    # 南京邮电大学
    
    link = "http://njupt.91job.org.cn/"
    soup = get_link_content(link, '南京邮电大学')
    info_urls = soup.find_all(attrs={'id': 'tabs-d'})
    lis_list = info_urls[0].find_all('li')
    
    youdian_info_list = []
    for items in lis_list:
        context = {}
        aTag_s = items.find_all("a")
        context['title'] = aTag_s[1].string
        context['time'] = items.span.string
        context['address'] = aTag_s[0].string
        context['detail'] = link[:-1] + aTag_s[1].attrs['href']
        youdian_info_list.append(context)
    
    
    tmp = """<!DOCTYPE html>
    <html> 
        <head> 
            <meta charset="utf-8"/>  
            <title>宣讲会信息</title>
        </head> 
    <body>"""
    
    tmp = format_HTML(tmp, dongnan_info_list, '东南大学')

    tmp = format_HTML(tmp, gongye_info_list, '南京工业大学')
    
    tmp = format_HTML(tmp, nongye_info_list, '南京农业大学')
    
    tmp = format_HTML(tmp, youdian_info_list, '南京邮电大学')
    
    tmp += """</body> 
    </html>"""

    # 'lijzwushang@163.com','qinyuaq@163.com'
    listeners = ['1971328641@qq.com']

    for i in listeners:
        send_emails(tmp, i)
        print("{} 发送成功".format(i))
    return 'Hello, World!'








