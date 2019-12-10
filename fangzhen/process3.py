import time
import os
import shutil
import re
import winsound
from Common import *
from loguru import logger
from write_logging import Date_Time
from Init import All_Init
import pyautogui as png
import random
import cv2 as cv
from utils.baidu_ocr import get_text_by_img
from write_file_png import Image_Process
image_stances = Image_Process()
os.chdir(HOME_DIR)

def make_wrapper(func):
    def wrapper(*args, **kwargs):
        args_list = list(args)
        new_args = []
        for i, item in enumerate(args_list):
            if i in [1, 3]:
                new_args.append(item+41)  # +58是自动化  +50标签栏  -41firefox +17benren 
            else:
                new_args.append(item)
        func(*new_args)
    return wrapper

@make_wrapper
def save_picture(x1, y1, x2, y2, user_dir, name):
    """
    截图保存功能，默认保存在self.user_dir
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :param name: 图片名称
    :return:
    """
    mouse_click(1350, 900)
    assert isinstance(name, str)
    image_stances.save_png(image_stances.shoot_png(x1, y1, x2, y2), user_dir, name)
    time.sleep(1)


@make_wrapper
def mouse_click(x1, y1):
    png.moveTo(x1, y1, duration=1)
    png.click()
    time.sleep(1)


@make_wrapper
def pull_mouse(x1, y1, x2, y2):
    """拖动"""
    png.moveTo(x1, y1, duration=1)
    png.dragTo(x2, y2, duration=3)


def mouse_click_and_input_content(x, y, content):
    """
    点击输入框并输入内容
    :param x:
    :param y:
    :param content:
    :return:
    """
    mouse_click(x, y)
    input_content(content)


def much_mouse_click(x1, y1, count, time_length=10):
    for i in range(count):
        time.sleep(time_length)
        mouse_click(x1, y1)
    time.sleep(10)


def input_content(number_str):
    """
    写入输入框
    :param number_str: 156.62
    :return: Null
    """
    time.sleep(1)
    for i in number_str:
        time.sleep(0.5)
        png.press(i)
    time.sleep(2)


def choose_to_rent(x1, y1):
    """
    点击子选项+租赁选项
    :param x1:
    :param y1:
    :return:
    """
    mouse_click(x1, y1)
    time.sleep(1)
    mouse_click(1133, 606)

def choose_to_buy(x1, y1):
    """
    点击子选项 + 购买选项
    :param x1:
    :param y1:
    :return:
    """
    mouse_click(x1, y1)
    time.sleep(1)
    mouse_click(1133, 577)
    # todo：待定 mouse_click()

def resource_chose_rent():
    """选择租赁"""
    # 生成随机值
    flag_number = random.randint(1, 3)
    # Step1:硬件资源配置
    mouse_click(720, 488)
    choose_to_rent(870, 488)
    choose_to_rent(870, 540)
    choose_to_rent(870, 590)
    choose_to_rent(870, 640)
    # Step2:软件资源配置
    mouse_click(720, 540)
    choose_to_rent(870, 488)
    choose_to_rent(870, 540)
    # Step3:网络资源配置
    mouse_click(720, 590)
    choose_to_rent(870, 488)
    choose_to_rent(870, 540)
    choose_to_rent(870, 590)
    choose_to_rent(870, 640)
    # Step4:运营资源配置
    mouse_click(720, 640)
    mouse_click(870, 490)  # 4.1计算
    choose_to_rent(1020, 492)
    choose_to_rent(1020, 532)
    choose_to_rent(1020, 568)
    mouse_click(870, 520)  # 4.2数据库
    choose_to_rent(1022, 492)
    choose_to_rent(1022, 531)
    choose_to_rent(1022, 570)
    choose_to_rent(1022, 610)
    mouse_click(870, 555)  # 4.3存储
    choose_to_rent(1020, 490)
    choose_to_rent(1020, 530)
    choose_to_rent(1020, 570)
    mouse_click(870, 590)  # 4.4域名服务
    choose_to_rent(1020, 495)
    choose_to_rent(1020, 530)
    mouse_click(870, 620)  # 4.5数据分析
    choose_to_rent(1020, 495)
    choose_to_rent(1020, 530)
    choose_to_rent(1020, 570)
    choose_to_rent(1020, 610)
    choose_to_rent(1020, 650)
    mouse_click(870, 650)  # 4.6安全防护
    choose_to_rent(1020, 493)
    choose_to_rent(1020, 530)
    choose_to_rent(1020, 570)
    pass

def resource_chose_buy():
    """选择购买"""
    # 生成随机值
    flag_number = random.randint(1, 3)
    # Step1:硬件资源配置
    mouse_click(720, 488)
    choose_to_buy(870, 488)
    choose_to_buy(870, 540)
    choose_to_buy(870, 590)
    choose_to_buy(870, 640)
    # Step2:软件资源配置
    mouse_click(720, 540)
    choose_to_buy(870, 488)
    choose_to_buy(870, 540)
    # Step3:网络资源配置
    mouse_click(720, 590)
    choose_to_buy(870, 488)
    choose_to_buy(870, 540)
    choose_to_buy(870, 590)
    choose_to_buy(870, 640)
    # Step4:运营资源配置
    mouse_click(720, 640)
    mouse_click(870, 490)  # 4.1计算
    choose_to_buy(1020, 492)
    choose_to_buy(1020, 532)
    choose_to_buy(1020, 568)
    mouse_click(870, 520)  # 4.2数据库
    choose_to_buy(1022, 492)
    choose_to_buy(1022, 531)
    choose_to_buy(1022, 570)
    choose_to_buy(1022, 610)
    mouse_click(870, 555)  # 4.3存储
    choose_to_buy(1020, 490)
    choose_to_buy(1020, 530)
    choose_to_buy(1020, 570)
    mouse_click(870, 590)  # 4.4域名服务
    choose_to_buy(1020, 495)
    choose_to_buy(1020, 530)
    mouse_click(870, 620)  # 4.5数据分析
    choose_to_buy(1020, 495)
    choose_to_buy(1020, 530)
    choose_to_buy(1020, 570)
    choose_to_buy(1020, 610)
    choose_to_buy(1020, 650)
    mouse_click(870, 650)  # 4.6安全防护
    choose_to_buy(1020, 493)
    choose_to_buy(1020, 530)
    choose_to_buy(1020, 570)


def select_option(x1, y1, x2, y2):
    mouse_click(x1, y1)
    mouse_click(x2, y2)


def judge_load_status():

    pass


def basis(user_dir):

    # 点击开始
    mouse_click(941, 539)

    # 完整流程
    time.sleep(2)
    mouse_click(798, 541)
    time.sleep(20)

    # 开始页面截图
    save_picture(466, 272, 1420, 804, user_dir, '开始页面')
    time.sleep(5)
    mouse_click(1116, 760)
    time.sleep(90)  # 加载时间较长

    # much_mouse_click(1116, 760, 23)
    much_mouse_click(1116, 760, 5, 5)
    time.sleep(15)
    mouse_click(1116, 760)
    time.sleep(15)
    much_mouse_click(1116, 760, 3, 10)
    much_mouse_click(1116, 760, 4, 5)
    much_mouse_click(1116, 760, 1, 10)
    much_mouse_click(1116, 760, 9, 5)



# basis('C:\\Users\\jvlunl\\Desktop\\test1\\仿真系统\\resources\\20191106\\15251853026')


def resource_configuration_module():
    """资源配置模块"""
    # 填写用户人数
    mouse_click_and_input_content(950, 653, '120132')
    # 点击提交
    mouse_click(1228, 684)
    # 点击下一步
    mouse_click(946, 688)
    # 点击业务预测框
    mouse_click_and_input_content(1100, 657, '147464')
    # 点击提交
    mouse_click(1240, 710)
    # 点击下一步
    mouse_click(1130, 668)
    time.sleep(2)
    # 查看资源配置图后点击确定
    mouse_click(1230, 730)
    # 点击开始配置资源
    mouse_click(1330, 643)
    # ------------开始配置资源-----------------
    # todo:选择购买或者租赁
    if '资源配置.png' in os.listdir(os.path.dirname(RESOURCES_SETTING_PNG)):
        os.rename(RESOURCES_SETTING_PNG, os.path.join(os.path.dirname(RESOURCES_SETTING_PNG), str(time.time()).replace('.', '')+'.png'))
    time.sleep(5)
    # todo:坐标待测试
    save_picture(1083, 437, 1179, 457, os.path.dirname(RESOURCES_SETTING_PNG), '资源配置')
    time.sleep(5)

    # 获取文字识别结果
    result_list = get_text_by_img(RESOURCES_SETTING_PNG)
    if '成长期' in result_list or '成熟期' in result_list or '持续发展期' in result_list:
        resource_chose_buy()
    else:
        resource_chose_rent()

    # 点击提交
    mouse_click(1200, 710)
    time.sleep(10)
    # 点击确认
    mouse_click(945, 648)
    time.sleep(10)
    # 资源配置模式选择
    select_option(1177, 465, 1113, 511)
    mouse_click_and_input_content(1156, 542, '1040')
    # 点击提交
    mouse_click(1230, 720)
    mouse_click(1180, 653)

    # 优化循环
    # much_mouse_click(1116, 760, 7)
    mouse_click(1116, 760)
    much_mouse_click(1116, 760, 1, 10)
    mouse_click(1116, 760)
    much_mouse_click(1116, 760, 1, 10)
    much_mouse_click(1116, 760, 3, 2)




def business_design_module():
    """业务设计模块"""
    # action1:填写预计套餐费用
    mouse_click_and_input_content(650, 615, '95')
    pull_mouse(712, 611, 747, 607)
    pull_mouse(816, 613, 834, 613)
    mouse_click(943, 727)
    mouse_click_and_input_content(650, 615, '55')
    pull_mouse(712, 611, 729, 607)
    pull_mouse(816, 613, 834, 613)
    mouse_click(943, 727)
    mouse_click_and_input_content(650, 615, '28')
    pull_mouse(712, 611, 717, 607)
    mouse_click(943, 727)
    much_mouse_click(1116, 760, 4)
    # action2:业务流程设计
    mouse_click(935, 582)
    mouse_click(1116, 760)
    # todo: 根据字段识别顺序，拉动
    # 1. 截图保存，先重命名原截图，再截取保存
    if '产品流程.png' in os.listdir(os.path.dirname(PRODUCT_FLOW_PNG)):
        os.rename(PRODUCT_FLOW_PNG, os.path.join(os.path.dirname(PRODUCT_FLOW_PNG), str(time.time()).replace('.', '')+'.png'))
    time.sleep(5)
    save_picture(631, 375, 773, 680, os.path.dirname(PRODUCT_FLOW_PNG), '产品流程')
    time.sleep(2)

    # 2. 获取字段顺序，拖动
    result_list = get_text_by_img(PRODUCT_FLOW_PNG)
    from_index = [[609, 395], [615, 437], [610, 481],
                  [608, 528], [615, 569], [612, 618],
                  [610, 663]]
    # 选定目标用户群
    if '选定目标用户群' in result_list:
        if result_list.index('选定目标用户群') < 7:
            pull_mouse(*from_index[result_list.index('选定目标用户群')], 899, 460)
    # result_list.index('选定目标用户群')
    # 对用户群调研
    if '对用户群体进行调研' in result_list:
        if result_list.index('对用户群体进行调研') < 7:
        
            pull_mouse(*from_index[result_list.index('对用户群体进行调研')], 1020, 463)
    # result_list.index('对用户群体进行调研')
    # 设计产品实例
    if '设计产品实例' in result_list:
        if result_list.index('设计产品实例') < 7:
            pull_mouse(*from_index[result_list.index('设计产品实例')], 1146, 463)
    # result_list.index('设计产品实例')
    # 指定定价策略
    if '制定定价策略' in result_list:
        if result_list.index('制定定价策略') < 7:
            pull_mouse(*from_index[result_list.index('制定定价策略')], 1270, 463)
    # result_list.index('制定定价策略')
    # 产品测试
    if '产品测试' in result_list:
        if result_list.index('产品测试') < 7:
            pull_mouse(*from_index[result_list.index('产品测试')], 897, 595)
    # result_list.index('产品测试')
    # 产品优化
    if '产品优化' in result_list:
        if result_list.index('产品优化') < 7:
            pull_mouse(*from_index[result_list.index('产品优化')], 1023, 595)
    # result_list.index('产品优化')
    # 产品推广
    if '产品推广' in result_list:
        if result_list.index('产品推广') < 7:
        
            pull_mouse(*from_index[result_list.index('产品推广')], 1150, 595)
    # result_list.index('产品推广')
    mouse_click(1268, 674)
    mouse_click(1037, 614)
    mouse_click(1116, 760)
    # todo: 选择字段，判断字段是否是随机的,是随机分布
    mouse_click(1272, 673)
    mouse_click(1270, 647)
    if random.randint(1, 2) == 2:  # 错误选择
        mouse_click(1275, 617)
    else:
        mouse_click(1270, 589)  # 第三个无效字段
    # 点击确认
    mouse_click(1325, 746)
    time.sleep(2)
    much_mouse_click(1116, 760, 5, 2)
    mouse_click(953, 572)
    much_mouse_click(1116, 760, 2, 2)
    time.sleep(10)
    # action3:字段分析
    # todo:数据面板展示流程需要debug
    # 点击新业务费
    mouse_click(737, 436)
    mouse_click(574, 549)
    mouse_click(641, 324)
    mouse_click(1345, 778)
    much_mouse_click(1116, 760, 4, 3)
    mouse_click(1264, 790)
    # mouse_click_and_input_content(1025, 787, '250004443241')
    # 业务号是随机的，需要模拟点击
    time.sleep(5)
    mouse_click(640, 468)
    # 提交
    mouse_click(1370, 790)
    time.sleep(2)

    much_mouse_click(1116, 760, 8, 3)
    # 开始业务设计
    mouse_click(946, 550)
    mouse_click(952, 634)
    much_mouse_click(1116, 760, 2)
    mouse_click(945, 561)
    much_mouse_click(1116, 760, 6)
    # 流失分析
    mouse_click_and_input_content(1189, 466, '64')
    mouse_click_and_input_content(1189, 513, '14')
    mouse_click_and_input_content(1189, 560, '27')
    mouse_click_and_input_content(1189, 611, '56')
    mouse_click(1196, 671)
    pull_mouse(713, 747, 548, 746)
    mouse_click(592, 735)
    mouse_click(708, 727)
    mouse_click(823, 730)
    mouse_click(938, 730)
    mouse_click(1050, 729)
    # 点击生成
    mouse_click(1232, 740)
    mouse_click(1312, 739)
    # action4:设计挽留业务
    mouse_click_and_input_content(826, 506, '9')
    mouse_click_and_input_content(970, 506, '9')
    mouse_click_and_input_content(1150, 506, '9')
    mouse_click_and_input_content(824, 557, '9')
    mouse_click_and_input_content(966, 557, '9')
    mouse_click_and_input_content(1153, 557, '9')
    mouse_click_and_input_content(827, 608, '9')
    mouse_click_and_input_content(968, 608, '9')
    mouse_click_and_input_content(1148, 608, '9')
    mouse_click(943, 659)
    much_mouse_click(1116, 760, 5)
    time.sleep(20)
    much_mouse_click(1116, 760, 3)
    time.sleep(10)
    much_mouse_click(1116, 760, 2)


def marketing_module():
    """市场推广模块"""
    mouse_click_and_input_content(1307, 611, '0.1')
    mouse_click_and_input_content(1306, 650, '1590.16')
    mouse_click_and_input_content(1299, 684, '1027.38')
    mouse_click_and_input_content(1307, 715, '1391.58')
    mouse_click(1298, 758)
    time.sleep(10)
    mouse_click(1170, 662)
    time.sleep(10)
    mouse_click(1116, 760)
    time.sleep(10)
    # 业务定价
    # 先设定条件
    mouse_click(617, 489)
    time.sleep(1)
    mouse_click(599, 545)
    time.sleep(1)
    mouse_click(569, 606)
    time.sleep(1)
    mouse_click(639, 666)
    time.sleep(2)
    mouse_click_and_input_content(1104, 515, '0.24')
    mouse_click_and_input_content(1271, 516, '0.6')
    mouse_click_and_input_content(1104, 553, '0.22')
    mouse_click_and_input_content(1277, 554, '0.55')
    mouse_click_and_input_content(1104, 593, '0.3')
    mouse_click_and_input_content(1269, 594, '0.75')
    mouse_click(1110, 664)
    time.sleep(5)
    mouse_click(944, 725)
    mouse_click(1116, 760)
    time.sleep(5)
    # 产品推广方式
    mouse_click_and_input_content(1026, 494, '5')
    mouse_click_and_input_content(1028, 553, '5')
    mouse_click(946, 599)
    time.sleep(5)
    mouse_click(1116, 760)
    # 产品收益表
    mouse_click_and_input_content(768, 629, '489683')
    mouse_click_and_input_content(861, 626, '367119')
    mouse_click_and_input_content(958, 628, '244755')
    mouse_click_and_input_content(769, 655, '167315.4')
    mouse_click_and_input_content(865, 655, '111558.6')
    mouse_click_and_input_content(955, 657, '55801.8')
    mouse_click_and_input_content(772, 683, '23760')
    mouse_click_and_input_content(863, 684, '15840')
    mouse_click_and_input_content(946, 686, '7920')
    mouse_click(1217, 685)
    time.sleep(5)
    much_mouse_click(1116, 760, 2, 2)
    # 风险控制原则
    select_option(1297, 547, 1277, 638)
    select_option(1278, 590, 1281, 651)
    select_option(1285, 632, 1263, 712)
    select_option(1311, 678, 1284, 748)
    # 点击提交
    mouse_click(1321, 744)
    time.sleep(5)
    mouse_click(941, 700)
    time.sleep(5)
    much_mouse_click(1116, 760, 2)
    time.sleep(30)

# marketing_module()

def profit_and_loss_measurement_module():
    """损益测算模块"""
    much_mouse_click(1116, 760, 9, 3)
    time.sleep(5)
    # 调整概率
    pull_mouse(908, 460, 945, 456)
    pull_mouse(885, 498, 908, 501)
    mouse_click_and_input_content(941, 597, '21088.550')
    mouse_click_and_input_content(943, 623, '7039.944')
    mouse_click_and_input_content(942, 658, '18216.000')
    mouse_click(943, 698)
    time.sleep(5)
    mouse_click(946, 712)
    time.sleep(5)
    # 设定计算参数
    mouse_click(1074, 469)
    mouse_click(1074, 498)
    mouse_click_and_input_content(1121, 557, '40')
    mouse_click_and_input_content(1124, 591, '800')
    mouse_click_and_input_content(1121, 622, '2540')
    mouse_click(943, 657)
    time.sleep(5)
    mouse_click(946, 650)
    time.sleep(5)
    # 计算变动成本
    pull_mouse(980, 519, 997, 517)
    mouse_click_and_input_content(947, 601, '2000')
    mouse_click(951, 655)
    time.sleep(5)
    mouse_click(947, 655)
    # 产品损益表
    mouse_click_and_input_content(995, 540, '16548.550')
    mouse_click_and_input_content(997, 564, '2499.944')
    mouse_click_and_input_content(993, 586, '13676.000')
    mouse_click(943, 635)
    time.sleep(2)
    mouse_click(1180, 734)
    mouse_click(1256, 722)
    much_mouse_click(1116, 760, 3, 2)
    time.sleep(2)
    much_mouse_click(1116, 760, 2, 2)
    # 点击记录
    time.sleep(6)
    mouse_click(1049, 530)

# profit_and_loss_measurement_module(user_dir)



def submit_file_firefox_in_shiyanshi():
    png.moveTo(642, 1006, duration=1)
    png.click()
    time.sleep(10)    
    png.moveTo(67, 142, duration=2)
    png.click()
    png.moveTo(204, 140, duration=2)
    png.click()
    png.moveTo(777, 508, duration=2)
    png.click()
    time.sleep(20)
    png.moveTo(1911, 540, duration=1)
    png.dragTo(1911, 800, duration=3)
    time.sleep(10)
    # 点击提交
    png.moveTo(951, 907, duration=2)
    png.click()
    pass



time.sleep(30)
logger.info("前期配置开始")
basis('C:\\Users\\Public\\Pictures')

logger.info("资源配置开始")
resource_configuration_module()

logger.info("商业配置开始")
business_design_module()

logger.info("市场配置开始")
marketing_module()

logger.info("利润损失配置开始")
profit_and_loss_measurement_module()


time.sleep(30)
winsound.Beep(300, 1000)
input("准备开始提交流程: ")
submit_file_firefox_in_shiyanshi()


time.sleep(40)
save_picture(0, 0, 1900, 900, 'C:\\Users\\Public\\Pictures', '实验成绩截图')
time.sleep(10000)







