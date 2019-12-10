import time
import os
import threading
import queue
from Common import *
from loguru import logger
from write_logging import Date_Time
from write_file_png import Image_Process
from Init import All_Init
import pyautogui as png
from selenium import webdriver
from chaojiying import Chaojiying_Client
import base64
"""
# 流程：
0. 初始化，读取任务列表流程，创建存储对象
层级：
 文件夹 > 用户存储文件夹(账号)

1. 登陆流程（browser, number）, 
2. 三连流程（browser, number）,

这两个任务都放在一个子线程函数中执行,这样不会破坏终止主线程


"""

IP = Image_Process()

def having_and_click(browser, css_selector):
    """
    判断该css-selector是否存在，存在则点击
    :param browser:
    :param css_selector:
    :return:
    """
    try:
        browser.find_element_by_css_selector(css_selector).click()
    except:
        logger.error('选择器 {} 不存在，页面可能加载失败'.format(css_selector))
        raise

def password_detection(browser, user_name):
    """
    由于密码多次试错+验证码可选问题逻辑较复杂，
    故增加密码探测流程
    一旦错误，退出浏览器，重新打开
    :return: 正确密码
    """
    for index, password in enumerate(['12345678', 'Njupt123', '11111111']):
        link = 'http://www.ilab-x.com/login'
        browser.get(link)
        time.sleep(8)
        browser.maximize_window()
        while not browser.find_elements_by_css_selector('#user'):
            browser.refresh()
            time.sleep(10)
        user = browser.find_element_by_css_selector('#user')
        time.sleep(1)
        passwd = browser.find_element_by_css_selector('#password')
        time.sleep(1)
        logger.info("用户：{}, 进行第 {} 次密码探测".format(user_name, index + 1))
        user.clear()
        user.send_keys(user_name)
        time.sleep(0.5)
        passwd.clear()
        passwd.send_keys(password)
        time.sleep(1)

        # --------------------------
        while True:
            # time.sleep(30)
            # todo:准备调用超级鹰打码API
            # 截图保存验证码,用时间戳命名
            # 调用API，返回识别码
            # todo:采集base64保存为图片
            img = browser.find_element_by_css_selector('#loginForm > div.login_item.item-verify.hide > span > img')
            img_code = img.get_attribute('src')
            png_base64 = img_code.split('jpeg;base64,')[1]  # 获取验证码图片的base64编码
            IP.save_png_from_base64_to_picture(png_base64=png_base64)
            time.sleep(5)
            chaojiying = Chaojiying_Client(chao_user, chao_passwd, app_id)
            im = open(IP.get_newest_login_file(), 'rb').read()
            key_code = chaojiying.PostPic(im, 1902)['pic_str']
            if browser.find_elements_by_css_selector("#loginForm > div.login_item.item-verify.hide > input"):
                browser.find_element_by_css_selector("#loginForm > div.login_item.item-verify.hide > input").clear()
                browser.find_element_by_css_selector("#loginForm > div.login_item.item-verify.hide > input").send_keys(key_code)
            time.sleep(5)
            browser.find_element_by_css_selector("#loginBut").click()
            time.sleep(25)
            info_text = browser.execute_script("""return document.querySelector('#dialog_content').innerText""")
            if browser.current_url == 'http://www.ilab-x.com/':
                logger.info('用户：{} , 密码：{} 探测成功'.format(user_name, password))
                return password
            elif info_text == '验证码错误':
                browser.find_element_by_css_selector('#dialog_ok').click()
                browser.find_element_by_css_selector(".verify-code > img:nth-child(1)").click()
                continue
            else:
                break


def before_after_test(user_name, q):
    """
    检测该用户是否完成实验
    1. 任务开始前
    2. 任务完成后
    :return:
    """
    browser = webdriver.Chrome()
    try:
        password = password_detection(browser, user_name)
        if not password:
            logger.error("用户： {}登陆失败，记录，等待下次测试，可能原因：超时，密码未修正".format(user_name))
            q.put(-1)
            # return -1
        # link = 'http://www.ilab-x.com/login'
        # browser.get(link)
        browser.maximize_window()
        # 查看实验记录或成绩
        browser.find_element_by_css_selector('#username').click()
        logger.info("用户 {}, 点击进入用户页面".format(user_name))
        time.sleep(10)

        # #left-menu > div > ul > li.m-li8 > a
        browser.find_element_by_css_selector('#left-menu > div > ul > li.m-li8 > a').click()
        logger.info("用户 {}, 点击左侧菜单查看成绩信息".format(user_name))
        time.sleep(10)
        if len(browser.find_elements_by_css_selector('#list > li > div.info > div.btns > span:nth-child(3)')) >= 1:
            grade_buttom = browser.find_element_by_css_selector('#list > li > div.info > div.btns > span:nth-child(3)')
            time.sleep(5)  # #list > li > div.info > div.btns > span:nth-child(3)
            grade_buttom.click()
            logger.info("用户 {}, 点击我的成绩按钮".format(user_name))
            time.sleep(10)
            if browser.find_elements_by_css_selector('#uList > table > tbody > tr:nth-child(2)'):
                tr_css = browser.find_element_by_css_selector('#uList > table > tbody > tr:nth-child(2)')
                logger.info("用户: {} 查询结果： {}".format(user_name, tr_css.text))
                grade = int(tr_css.text.split()[2])
                if grade < 60:
                    logger.error("用户: {} 仿真实验测试成绩： {}".format(user_name, grade))
            else:
                if browser.find_elements_by_css_selector("#search > span"):
                    browser.find_element_by_css_selector("#search > span").click()
                    time.sleep(2)
                q.put(0)  # 未做测试
                logger.debug('用户 :{} 需要重新检测，为获取到成绩信息'.format(user_name))
            san_lian(browser, number)
            q.put(1)  # 已经做过
        else:
            logger.debug('用户 :{} 需要重新检测，为获取到成绩信息'.format(user_name))
            q.put(0)  # 未做测试
        browser.close()
    except:
        browser.close()



def san_lian(browser, number):
    time.sleep(5)
    having_and_click(browser, "#search > span")
    time.sleep(5)
    # 点击进入项目
    having_and_click(browser, '#list > li > div.info > div.btns > a')
    time.sleep(20)
    windows = browser.window_handles
    browser.switch_to.window(windows[-1])
    cur_url = browser.current_url
    logger.info("用户 {} 跳转到页面标签(实验评价页面) {} ".format(number, cur_url))
    time.sleep(10)
    having_and_click(browser, '#likeBtn')
    logger.info('用户 {} 点赞操作完成'.format(number))
    time.sleep(2)
    js = 'window.scrollTo(0,500)'
    browser.execute_script(js)
    time.sleep(5)
    # 判断是否点赞
    if browser.find_elements_by_css_selector('#evaluate > h5'):
        # todo:评分
        browser.find_element_by_css_selector('#evaluate > a > div > span:nth-child(5)').click()
        time.sleep(3)
        if browser.find_elements_by_css_selector("#dialog_ok"):
            browser.find_element_by_css_selector("#dialog_ok").click()
            time.sleep(3)
        logger.info("用户 ：{} 自动化评分完成".format(number))
    else:
        logger.info("用户 ：{} 已经评分完成".format(number))

    if browser.find_elements_by_css_selector("#commentForm > textarea"):
        # todo:评论
        browser.execute_script("""document.querySelector("#commentForm > textarea").value = '好'""")
        time.sleep(2)
        browser.find_element_by_css_selector('#btn-subComment').click()
        time.sleep(2)
        logger.info("用户 ：{} 自动化评价完成".format(number))
    else:
        logger.info("用户 ：{} 已经评价完成".format(number))



dt = Date_Time()
status_list_dict = {}
info_list = dt.get_number_from_dir(OS_PATH)

for aindex, number in enumerate(info_list):
    q = queue.Queue()
    # 子线程执行 校验流程
    try:
        threadA = threading.Thread(target=before_after_test, args=(number, q))
        threadA.start()
        threadA.join()
    except:
        pass
    test_code = -1
    if not q.empty():
        test_code = q.get()
    logger.info("用户: {} before_after_test执行完毕, test_code:{}".format(number, test_code))
    time.sleep(1000)


    







"""
img_code = img.get_attribute('src')
img_code.split('jpeg;base64,')

>>> aa = bytes(a, encoding='utf-8')
>>> b = base64.b64decode(aa)

>>> file = open('bb.png', 'wb')                                                                                         
>>> file.write(b)
4015
>>> file.close()

"""




















