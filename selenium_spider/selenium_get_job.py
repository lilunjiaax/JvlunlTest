import time
import sys
from selenium import webdriver
from urllib.parse import quote
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait

import requests

from bs4 import BeautifulSoup
import random
from email.mime.text import MIMEText

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib



# URL_dict = {'南京工业大学': 'http://seu.91job.org.cn/teachin'}




# browser.get("https://www.baidu.com")
# browser.maximize_window()

# time.sleep(100)

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


def nanda_get_link_content(link, school_name):

    headers = {
        'Cookie': 'route=e0874f8f82f1d5dacc07606f33782719; SESSION=02c138cb-9f7e-4dd9-adf1-c28e051f2069; JSESSIONID=DECD9A3544BD08787F56FF127E7837AF',
'Host': 'job.nju.edu.cn',
'Origin': 'http://job.nju.edu.cn',
'Proxy-Connection': 'keep-alive',
'Referer': 'http://job.nju.edu.cn/',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
    }
    response = requests.get(link, headers=headers, verify=False, timeout=10) 
    time.sleep(random.randint(0, 3))
    print(school_name, 'status_code:', response.status_code)
    html_text = response.text
    soup = BeautifulSoup(html_text, 'lxml')
    return soup




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

# 南京财经大学
link = 'http://njue.91job.org.cn/'
soup = get_link_content(link, '南京财经大学')
info_urls = soup.find_all(attrs={'id': 'tabs-23'})
lis_list = info_urls[0].find_all('li')

nancai_info_list = []

for item in lis_list:
    context = {}
    aTag_s = item.find_all('a')
    context['title'] = aTag_s[1].string
    context['time'] = item.span.string
    context['address'] = aTag_s[0].string
    context['detail'] = link[:-1] + aTag_s[1].attrs['href']
    nancai_info_list.append(context)

"""
[<ul class="tabCon hide" id="tabs-23">
<li>
<span class="pubdate">2019-11-06</span>
<a class="it2" href="/teachin/view/id/198501" title="南京艺德源动漫制作有限公司">南京财经大学仙林校区大学生活动中心116招聘室</a>
<a href="/teachin/view/id/198501">南京艺德源动漫制作有限公司</a>
</li>

"""

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


# 南京大学

def get_nanda_info():

    browser = webdriver.Chrome()
    link = 'http://job.nju.edu.cn/#!/more/special_recruit'
    # soup = get_link_content(link, '南京大学')
    # info_urls = soup.select('.news-list ul')
    # print(info_urls.find_all('li'))

    browser.get(link)
    
    browser.maximize_window()
    # time.sleep(2)
    # home_page_css_selector = "#header > div.recruit-top > div.header_right > div > div.btn_home"
    # browser.find_elements_by_css_selector(home_page_css_selector)[0].click()
    #time,sleep(2)
    #mach_css_selector = "#main > div.ng-scope > div.index_jobs.ng-scope > div > div > div:nth-child(1) > h2 > a > span"
    #browser.find_elements_by_css_selector(mach_css_selector)[0].click()
    #time.sleep(2)
    #special_css_selector = "#bs-example-navbar-collapse-1 > ul > li.ng-scope.active > a"
    #browser.find_elements_by_css_selector(special_css_selector)[0].click()
    #time.sleep(2)
    
    
    time.sleep(20)
    browser.refresh()
    time.sleep(20)
    browser.refresh()
    time.sleep(10)
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


info_str = """<!DOCTYPE html>
<html> 
    <head> 
        <meta charset="utf-8"/>  
        <title>宣讲会信息</title>
    </head> 
<body> 
<table>
  <tbody>
    <tr>
      <td>January</td>
      <td>$100</td>
    </tr>
    <tr>
      <td>February</td>
      <td>$80</td>
    </tr>
  </tbody>
</table>
</body> 
</html>

"""
tmp = """<!DOCTYPE html>
<html> 
    <head> 
        <meta charset="utf-8"/>  
        <title>宣讲会信息</title>
    </head> 
<body>"""

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
  

 
tmp = format_HTML(tmp, dongnan_info_list, '东南大学')

tmp = format_HTML(tmp, gongye_info_list, '南京工业大学')

tmp = format_HTML(tmp, nongye_info_list, '南京农业大学')

tmp = format_HTML(tmp, youdian_info_list, '南京邮电大学')

tmp = format_HTML(tmp, nanda_info_list, '南京大学')

tmp = format_HTML(tmp, nancai_info_list, '南京财经大学')
tmp += """</body> 
</html>"""


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
    msg['Subject'] = Header('宣讲会信息……', 'utf-8').encode()
    
    server = smtplib.SMTP_SSL(smtp_server)
    # server.set_debuglevel(1)

    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


listeners = ['qinyuaq@163.com']

for i in listeners:
    send_emails(tmp, i)
    print("{} 发送成功".format(i))










