
import time
import os
import shutil
import re
import winsound
from Common import *
from loguru import logger
from write_logging import Date_Time
from Init import All_Init
import pyautogui as pag
import cv2 as cv
from selenium import webdriver
import collections
from process import save_picture
from write_file_png import Image_Process
image_stances = Image_Process()
from chaojiying import Chaojiying_Client


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
            save_picture(1065, 426, 1181, 467, LOGIN_IMG, str(time.time()).replace('.', ''))
            # image_stances.save_png(image_stances.shoot_png(1065, 484, 1181, 525), LOGIN_IMG, str(time.time()).replace('.', ''))
            time.sleep(5)
            chaojiying = Chaojiying_Client(chao_user, chao_passwd, app_id)
            im = open(image_stances.get_newest_login_file(), 'rb').read()
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



def judge_select(browser):
    info_text = browser.execute_script("""return document.querySelector('#dialog_content').innerText""")
    is_img = browser.execute_script('return document.querySelectorAll("#loginForm > div.login_item.item-verify.hide > span > img").length')
    if is_img == 1 and not info_text:
        # 无提示信息，只有输验证码
        return 1
    if is_img == 1 and info_text:
        # 出现错误提示
        return 0
    return 0


def before_after_test(browser, user_name, q):
    """
    检测该用户是否完成实验
    1. 任务开始前
    2. 任务完成后
    :return:
    """
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
    time.sleep(2)

    browser.find_element_by_css_selector('#left-menu > div > ul > li.m-li8 > a').click()
    logger.info("用户 {}, 点击左侧菜单查看成绩信息".format(user_name))
    time.sleep(5)
    if len(browser.find_elements_by_css_selector('#list > li > div.info > div.btns > span:nth-child(3)')) >= 1:
        grade_buttom = browser.find_element_by_css_selector('#list > li > div.info > div.btns > span:nth-child(3)')
        time.sleep(5)  # #list > li > div.info > div.btns > span:nth-child(3)
        grade_buttom.click()
        logger.info("用户 {}, 点击我的成绩按钮".format(user_name))
        time.sleep(5)

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
            enter_detail_page(browser, user_name)
            q.put(0)  # 未做测试
        q.put(1)  # 已经做过

    else:
        enter_detail_page(browser, user_name)
        q.put(0)  # 未做测试

    # time.sleep(10000)


def enter_detail_page(browser, user_name):
    logger.info("用户: {} 未作仿真实验测试".format(user_name))
    # #menu > li.nav_item.active > a
    browser.find_element_by_css_selector('#menu > li.nav_item.active > a').click()
    time.sleep(6)
    #   li.nav_item:nth-child(2) > a:nth-child(1)  firefix标签
    browser.find_element_by_css_selector('li.nav_item:nth-child(2) > a:nth-child(1)').click()
    time.sleep(10)

    # .school-title
    sousuo_input = browser.find_element_by_css_selector('.school-title')
    # #searchSection > div > div > div:nth-child(5) > div.edit > input.school-title
    sousuo_input.send_keys('黄卫东')
    time.sleep(2)
    # .s-btn
    browser.find_element_by_css_selector(".s-btn").click()
    # #searchSection > div > div > div:nth-child(5) > div.edit > button
    time.sleep(15)

    # .cover  .editbox
    # browser.find_element_by_css_selector(".editbox").click()
    # #list > li > a > div.cbox > div.pic > img
    winsound.Beep(550, 1000)
    input('请点击图片后输入 Y/N ： ')
    time.sleep(20)
    windows = browser.window_handles
    browser.switch_to.window(windows[-1])
    time.sleep(1)
    cur_url = browser.current_url
    logger.info("用户 {} 跳转到页面标签(实验评价页面) {} ".format(user_name, cur_url))
    # if like_comment(browser):
    #     logger.info("用户 {} , 已完成：点赞，评价，评语 ".format(user_name))
    if browser.find_elements_by_css_selector("#doBtn"):
        logger.info("用户 {} 跳转到页面标签,跳转成功 (实验评价页面) {} ".format(user_name, cur_url))
    browser.find_element_by_css_selector("#doBtn").click()  # #doBtn
    time.sleep(6)

    # .goLink-link > a:nth-child(1)
    if browser.find_elements_by_css_selector('.goLink-link > a:nth-child(1)'):
        browser.find_element_by_css_selector('.goLink-link > a:nth-child(1)').click()  # #dialog_content > p.goLink-link > a 跳转到实验界面的链接
    else:
        logger.error("用户 {} 在(实验评价页面)未获得跳转链接".format(user_name))
    logger.info("用户：{} 跳转到试验台页面".format(user_name))
    time.sleep(40)



def like_comment(browser):
    if 'http://www.ilab-x.com/details/' not in browser.current_url:        # 'http://www.ilab-x.com/details/v5?id=4160&isView=true'
        return False
    browser.find_element_by_css_selector('#likeBtn').click()
    time.sleep(1)

    browser.execute_script("""document.querySelector("#evaluate > a > div > span:nth-child(5)").click()""")
    # browser.find_element_by_css_selector("#evaluate > a > div > span:nth-child(5)").click()
    time.sleep(2)
    if len(browser.find_elements_by_css_selector("#dialog_ok")):
        browser.find_element_by_css_selector('#dialog_ok').click()
        time.sleep(1)
    browser.execute_script("""document.querySelector("#commentForm > textarea").value = '好'""")
    time.sleep(1)
    browser.find_element_by_css_selector('#btn-subComment').click()
    time.sleep(1)
    return True


def get_error_info_login(browser, user_name, password):
    login_error_info = browser.find_element_by_css_selector('#dialog_content')
    info_text = browser.execute_script("""return document.querySelector('#dialog_content').innerText""")
    if info_text:
        browser.find_element_by_css_selector('#dialog_ok').click()
    if login_error_info and info_text == '用户名或密码错误，请重新输入':
        logger.debug('用户：{} , 密码：{} 登陆失败, 失败原因：密码错误'.format(user_name, password))
        return 1
    if login_error_info and info_text == '验证码错误':
        logger.debug('用户：{} , 密码：{} 登陆失败, 失败原因：验证码错误'.format(user_name, password))
        return 2
    if login_error_info and info_text == '请填写验证码':
        logger.debug('用户：{} , 密码：{} 登陆失败, 失败原因：需填写验证码'.format(user_name, password))
        return 3
    return 0


def judge_login_status(browser, user_name, password):
    if browser.current_url == 'http://www.ilab-x.com/':
        logger.info('用户：{} , 密码：{} 登陆成功'.format(user_name, password))
        return True
    else:
        logger.debug('用户：{} , 密码：{} 登陆失败'.format(user_name, password))
        browser.refresh()
        time.sleep(6)
        return False


def send_keys_verify_code(browser, user_name, password):
    while True:
        logger.info('用户: {} 登陆时出现验证码'.format(user_name))
        #yanzhengma = input("请输入验证码: \n")
        #browser.find_element_by_css_selector('#loginForm > div.login_item.item-verify.hide > input').send_keys(yanzhengma)
        time.sleep(30)
        browser.find_element_by_css_selector("#loginBut").click()
        time.sleep(5)
        st1 = get_error_info_login(browser, user_name, password)
        if st1 == 0 and judge_login_status(browser, user_name, password):
            logger.info('用户：{} , 密码：{} 登陆成功'.format(user_name, password))
            return True
        if st1 == 2:
            continue
        if st1 == 1:
            return False


# option = webdriver.ChromeOptions()
# option.add_argument('disable-infobars')
# browser = webdriver.Chrome(chrome_options=option)
# number = '15251853026'
# before_after_test(browser, number)

