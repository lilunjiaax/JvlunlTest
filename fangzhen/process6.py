import time
import os
import shutil
import re
import winsound
from loguru import logger
import pyautogui as png
import random
from aip import AipOcr
from PIL import ImageGrab
"""
1. 缩短时间 27min
3. 双层装饰器实现自适应分辨率，使用相对位置比率来实现不同位置的移植，数据需要全部换掉，使用装饰器计算出每个数据的相对值

"""
def make_wrapper(func):
    def wrapper(*args, **kwargs):
        """
        实现自适应分辨率
        :param func:
        :param png: 屏幕操作对象，获取分辨率
        :return:
        """
        left_value, right_value, top_value, buttom_value = 464, 1425, 313, 853
        args_list = list(args)
        # 坐标的上下偏移
        new_args_one = []
        # 计算出相对坐标
        for i, item in enumerate(args_list):
            if isinstance(item, float):
                if i % 2 == 0:
                    new_args_one.append(int(left_value+(right_value-left_value)*item))
                if i % 2 == 1:
                    new_args_one.append(int(top_value+(buttom_value-top_value)*item))
            else:
                new_args_one.append(item)
        print('+==================+')
        print(new_args_one)
        func(*new_args_one)
    return wrapper

# 百度图像识别API_KEY
APP_ID = '17692081'
API_KEY = '4CGSRiGhYWGcDVsF8cGSr5AK'
SECRET_KEY = 'oDqztjaXhynRcVBmvADrZjmLZDlS3Rer'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_text_by_img(img_dir):
    with open(img_dir, 'rb') as fp:
        a = fp.read()
    options = {}
    options["detect_direction"] = "true"
    options["probability"] = "true"
    a_list = client.basicAccurate(a, options)['words_result']
    result_list = [item['words'] for item in a_list]
    return result_list

def shoot_png(x1, y1, x2, y2):
    """
    传入坐标，实现精准截图
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :return: <PIL.Image.Image image mode=RGB size=100x100 at 0x20BCD1D0F98>
    """
    bbox = (x1, y1, x2, y2)
    im = ImageGrab.grab(bbox)
    return im


def save_png(content, image_dir, png_name=''):
    """
    保存图片
    :param content: PIL image对象
    :param image_dir: 保存目录
    :return: 文件路径--> 存入日志
    """
    time.sleep(1)
    png_name = str(time.time()).split('.')[0]+'.png' if not png_name else png_name + '.png'
    png_dir = os.path.join(image_dir, png_name)
    content.save(png_dir)
    return png_dir


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
    mouse_click(0.921, 1.162)
    assert isinstance(name, str)
    save_png(shoot_png(x1, y1, x2, y2), user_dir, name)
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
    time.sleep(0.5)
    for i in number_str:
        time.sleep(0.2)
        png.press(i)
    time.sleep(1)


def choose_to_rent(x1, y1):
    """
    点击子选项+租赁选项
    :param x1:
    :param y1:
    :return:
    """
    mouse_click(x1, y1)
    time.sleep(1)
    mouse_click(0.696, 0.618)

def choose_to_buy(x1, y1):
    """
    点击子选项 + 购买选项
    :param x1:
    :param y1:
    :return:
    """
    mouse_click(x1, y1)
    time.sleep(1)
    mouse_click(0.696, 0.564)
    # todo：待定 mouse_click()

def resource_chose_rent():
    """选择租赁"""
    # Step1:硬件资源配置
    mouse_click(0.266, 0.4)
    choose_to_rent(0.422, 0.4)
    choose_to_rent(0.422, 0.496)
    choose_to_rent(0.422, 0.588)
    choose_to_rent(0.422, 0.681)
    # Step2:软件资源配置
    mouse_click(0.266, 0.496)
    choose_to_rent(0.422, 0.4)
    choose_to_rent(0.422, 0.496)
    # Step3:网络资源配置
    mouse_click(0.266, 0.588)
    choose_to_rent(0.422, 0.4)
    choose_to_rent(0.422, 0.496)
    choose_to_rent(0.422, 0.588)
    choose_to_rent(0.422, 0.681)
    # Step4:运营资源配置
    mouse_click(0.266, 0.681)
    mouse_click(0.422, 0.403)  # 4.1计算
    choose_to_rent(0.578, 0.407)
    choose_to_rent(0.578, 0.481)
    choose_to_rent(0.578, 0.548)
    mouse_click(0.422, 0.459)  # 4.2数据库
    choose_to_rent(0.58, 0.407)
    choose_to_rent(0.58, 0.479)
    choose_to_rent(0.58, 0.551)
    choose_to_rent(0.58, 0.625)

    mouse_click(0.422, 0.524)  # 4.3存储
    choose_to_rent(0.578, 0.403)
    choose_to_rent(0.578, 0.477)
    choose_to_rent(0.578, 0.551)
    mouse_click(0.422, 0.588)  # 4.4域名服务
    choose_to_rent(0.578, 0.421)
    choose_to_rent(0.578, 0.477)
    mouse_click(0.422, 620)  # 4.5数据分析
    choose_to_rent(0.578, 0.412)
    choose_to_rent(0.578, 0.477)
    choose_to_rent(0.578, 0.551)
    choose_to_rent(0.578, 0.625)
    choose_to_rent(0.578, 0.7)
    mouse_click(0.422, 0.7)  # 4.6安全防护
    choose_to_rent(0.578, 0.409)
    choose_to_rent(0.578, 0.477)
    choose_to_rent(0.578, 0.551)

def resource_chose_buy():
    """选择购买"""
    # Step1:硬件资源配置
    mouse_click(0.266, 0.4)
    choose_to_buy(870, 0.4)
    choose_to_buy(0.422, 0.496)
    choose_to_buy(0.422, 0.588)
    choose_to_buy(0.422, 0.681)
    # Step2:软件资源配置
    mouse_click(0.266, 0.496)
    choose_to_buy(0.422, 0.4)
    choose_to_buy(0.422, 0.496)
    # Step3:网络资源配置
    mouse_click(0.266, 0.588)
    choose_to_buy(0.422, 488)
    choose_to_buy(0.422, 0.496)
    choose_to_buy(0.422, 0.588)
    choose_to_buy(0.422, 0.681)

    # Step4:运营资源配置
    mouse_click(0.266, 0.681)
    mouse_click(0.422, 0.403)  # 4.1计算
    choose_to_buy(0.578, 0.407)
    choose_to_buy(0.578, 0.481)
    choose_to_buy(0.578, 0.548)
    mouse_click(0.422, 0.459)  # 4.2数据库
    choose_to_buy(0.578, 0.407)
    choose_to_buy(0.578, 0.481)
    choose_to_buy(0.578, 0.548)
    choose_to_buy(0.578, 610)
    mouse_click(0.422, 0.524)  # 4.3存储
    choose_to_buy(0.578, 0.407)
    choose_to_buy(0.578, 0.481)
    choose_to_buy(0.578, 0.548)
    mouse_click(0.422, 0.588)  # 4.4域名服务
    choose_to_buy(0.578, 0.407)
    choose_to_buy(0.578, 0.481)

    mouse_click(0.422, 0.644)  # 4.5数据分析
    choose_to_buy(0.578, 0.407)
    choose_to_buy(0.578, 0.481)
    choose_to_buy(0.578, 0.548)
    choose_to_buy(0.578, 0.625)
    choose_to_buy(0.578, 0.7)
    mouse_click(0.422, 0.7)  # 4.6安全防护
    choose_to_buy(0.578, 0.407)
    choose_to_buy(0.578, 0.481)
    choose_to_buy(0.578, 0.548)


def select_option(x1, y1, x2, y2):
    mouse_click(x1, y1)
    mouse_click(x2, y2)


def basis():
    # 点击开始
    mouse_click(0.496, 0.494)
    # 完整流程
    time.sleep(2)
    mouse_click(0.347, 0.498)
    time.sleep(20)
    time.sleep(5)
    mouse_click(0.678, 0.903)
    time.sleep(90)  # 加载时间较长

    much_mouse_click(0.678, 0.903, 5, 5)
    time.sleep(15)
    mouse_click(0.678, 0.903)
    time.sleep(15)
    much_mouse_click(0.678, 0.903, 3, 10)
    much_mouse_click(0.678, 0.903, 4, 5)
    much_mouse_click(0.678, 0.903, 1, 10)
    much_mouse_click(0.678, 0.903, 9, 5)


time.sleep(10)
basis()

def resource_configuration_module():
    """资源配置模块"""
    # 填写用户人数
    mouse_click_and_input_content(0.505, 0.705, '120132')
    # 点击提交
    mouse_click(0.795, 0.762)
    # 点击下一步
    mouse_click(0.501, 0.770)
    # 点击业务预测框
    mouse_click_and_input_content(0.661, 0.712, '147464')
    # 点击提交
    mouse_click(0.807, 0.811)
    # 点击下一步
    mouse_click(0.693, 0.733)
    time.sleep(2)
    # 查看资源配置图后点击确定
    mouse_click(0.797, 0.848)
    # 点击开始配置资源
    mouse_click(0.901, 0.687)
    # ------------开始配置资源-----------------
    # todo:选择购买或者租赁
    if '资源配置.png' in os.listdir(os.getcwd()):
        os.rename(os.path.join(os.getcwd(), '资源配置.png'), os.path.join(os.getcwd(), str(time.time()).replace('.', '')+'.png'))
    time.sleep(5)
    # todo:坐标待测试
    save_picture(0.644, 0.305, 0.744, 0.342, os.getcwd(), '资源配置')
    time.sleep(5)

    # 获取文字识别结果
    result_list = get_text_by_img(os.path.join(os.getcwd(), '资源配置.png'))
    if '成长期' in result_list or '成熟期' in result_list or '持续发展期' in result_list:
        resource_chose_buy()
    else:
        resource_chose_rent()

    # 点击提交
    mouse_click(0.765, 0.811)
    time.sleep(10)
    # 点击确认
    mouse_click(0.500, 0.696)
    time.sleep(10)
    # 资源配置模式选择
    select_option(0.741, 0.357, 0.675, 0.442)
    mouse_click_and_input_content(0.720, 0.5, '1040')
    # 点击提交
    mouse_click(0.797, 0.829)
    mouse_click(0.745, 0.705)

    # 优化循环
    mouse_click(0.678, 0.903)
    much_mouse_click(0.678, 0.903, 1, 10)
    mouse_click(0.678, 0.903)
    much_mouse_click(0.678, 0.903, 1, 10)
    much_mouse_click(0.678, 0.903, 3, 2)


def business_design_module():
    """业务设计模块"""
    # action1:填写预计套餐费用
    mouse_click_and_input_content(0.193, 0.635, '95')
    pull_mouse(0.258, 0.627, 0.294, 0.620)
    pull_mouse(0.366, 0.631, 0.385, 0.631)
    mouse_click(0.498, 0.842)
    mouse_click_and_input_content(0.193, 0.635, '55')
    pull_mouse(0.258, 0.627, 0.275, 0.620)
    pull_mouse(0.366, 0.631, 0.385, 0.631)
    mouse_click(0.498, 0.842)
    mouse_click_and_input_content(0.193, 0.635, '28')
    pull_mouse(0.258, 0.627, 0.263, 0.620)
    mouse_click(0.498, 0.842)
    much_mouse_click(0.678, 0.903, 4)
    # action2:业务流程设计
    mouse_click(0.490, 0.574)
    mouse_click(0.678, 0.903)
    # todo: 根据字段识别顺序，拉动
    # 1. 截图保存，先重命名原截图，再截取保存
    if '产品流程.png' in os.listdir(os.getcwd()):
        os.rename(os.path.join(os.getcwd(), '产品流程.png'), os.path.join(os.getcwd(), str(time.time()).replace('.', '')+'.png'))
    time.sleep(5)
    save_picture(0.173, 0.190, 0.321, 0.755, os.getcwd(), '产品流程')
    time.sleep(2)

    # 2. 获取字段顺序，拖动
    result_list = get_text_by_img(os.path.join(os.getcwd(), '产品流程.png'))
    from_index = [[0.151, 0.227], [0.151, 0.305], [0.151, 0.387],
                  [0.151, 0.474], [0.151, 0.55], [0.151, 0.640],
                  [0.151, 0.724]]
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
    mouse_click(0.836, 0.744)
    mouse_click(0.596, 0.633)
    mouse_click(0.678, 0.903)
    # todo: 选择字段，判断字段是否是随机的,是随机分布
    mouse_click(0.838, 0.742)
    mouse_click(0.838, 0.694)
    if random.randint(1, 2) == 2:  # 错误选择
        mouse_click(0.838, 0.638)
    else:
        mouse_click(0.838, 0.587)  # 第三个无效字段
    # 点击确认
    mouse_click(0.895, 0.877)
    time.sleep(2)
    much_mouse_click(0.678, 0.903, 5, 2)
    mouse_click(0.508, 0.555)
    much_mouse_click(0.678, 0.903, 2, 2)
    time.sleep(10)
    # action3:字段分析
    # todo:数据面板展示流程需要debug
    # 点击新业务费
    mouse_click(0.284, 0.303)
    mouse_click(0.114, 0.512)
    mouse_click(0.156, 0.096)
    mouse_click(0.916, 0.937)
    much_mouse_click(0.678, 0.903, 4, 3)
    mouse_click(0.832, 0.959)
    # mouse_click_and_input_content(1025, 787, '250004443241')
    # 业务号是随机的，需要模拟点击
    time.sleep(5)
    mouse_click(0.183, 0.362)
    # 提交
    mouse_click(0.942, 0.959)
    time.sleep(2)

    much_mouse_click(0.678, 0.903, 8, 3)
    # 开始业务设计
    mouse_click(0.501, 0.514)
    mouse_click(0.518, 0.670)
    much_mouse_click(0.678, 0.903, 2)
    mouse_click(0.501, 0.535)
    much_mouse_click(0.678, 0.903, 6)
    # 流失分析
    mouse_click_and_input_content(0.754, 0.359, '64')
    mouse_click_and_input_content(0.754, 0.446, '14')
    mouse_click_and_input_content(0.754, 0.533, '27')
    mouse_click_and_input_content(0.754, 0.627, '56')
    mouse_click(0.761, 0.738)
    pull_mouse(0.259, 0.879, 0.087, 0.877)
    mouse_click(0.133, 0.848)
    mouse_click(0.253, 0.848)
    mouse_click(0.373, 0.848)
    mouse_click(0.493, 0.848)
    mouse_click(0.609, 0.848)
    # 点击生成
    mouse_click(0.799, 0.866)
    mouse_click(0.882, 0.866)
    # action4:设计挽留业务
    mouse_click_and_input_content(0.376, 0.433, '9')
    mouse_click_and_input_content(0.524, 0.433, '9')
    mouse_click_and_input_content(0.713, 0.433, '9')
    mouse_click_and_input_content(0.376, 0.527, '9')
    mouse_click_and_input_content(0.524, 0.527, '9')
    mouse_click_and_input_content(0.713, 0.527, '9')
    mouse_click_and_input_content(0.376, 0.622, '9')
    mouse_click_and_input_content(0.524, 0.622, '9')
    mouse_click_and_input_content(0.713, 0.622, '9')
    mouse_click(0.498, 0.716)
    much_mouse_click(0.678, 0.903, 5)
    time.sleep(20)
    much_mouse_click(0.678, 0.903, 3)
    time.sleep(10)
    much_mouse_click(0.678, 0.903, 2)


def marketing_module():
    """市场推广模块"""
    mouse_click_and_input_content(0.869, 0.627, '0.1')
    mouse_click_and_input_content(0.869, 0.7, '1590.16')
    mouse_click_and_input_content(0.869, 0.762, '1027.38')
    mouse_click_and_input_content(0.869, 0.820, '1391.58')
    mouse_click(0.859, 0.9)
    time.sleep(10)
    mouse_click(0.734, 0.722)
    time.sleep(10)
    mouse_click(0.678, 0.903)
    time.sleep(10)
    # 业务定价
    # 先设定条件
    mouse_click(0.159, 0.410)
    time.sleep(1)
    mouse_click(0.140, 0.510)
    time.sleep(1)
    mouse_click(0.109, 0.618)
    time.sleep(1)
    mouse_click(0.182, 0.739)
    time.sleep(2)
    mouse_click_and_input_content(0.665, 0.45, '0.24')
    mouse_click_and_input_content(0.838, 0.45, '0.6')
    mouse_click_and_input_content(0.665, 0.520, '0.22')
    mouse_click_and_input_content(0.838, 0.520, '0.55')
    mouse_click_and_input_content(0.665, 0.594, '0.3')
    mouse_click_and_input_content(0.838, 0.594, '0.75')
    mouse_click(0.672, 0.725)
    time.sleep(5)
    mouse_click(0.499, 0.838)
    mouse_click(0.678, 0.903)
    time.sleep(5)
    # 产品推广方式
    mouse_click_and_input_content(0.584, 0.411, '5')
    mouse_click_and_input_content(0.584, 0.520, '5')
    mouse_click(0.501, 0.605)
    time.sleep(5)
    mouse_click(0.678, 0.903)
    # 产品收益表
    mouse_click_and_input_content(0.318, 0.659, '489683')
    mouse_click_and_input_content(0.415, 0.659, '367119')
    mouse_click_and_input_content(0.514, 0.659, '244755')
    mouse_click_and_input_content(0.318, 0.709, '167315.4')
    mouse_click_and_input_content(0.415, 0.709, '111558.6')
    mouse_click_and_input_content(0.514, 0.709, '55801.8')
    mouse_click_and_input_content(0.318, 0.762, '23760')
    mouse_click_and_input_content(0.415, 0.762, '15840')
    mouse_click_and_input_content(0.514, 0.762, '7920')
    mouse_click(0.783, 0.762)
    time.sleep(5)
    much_mouse_click(0.678, 0.903, 2, 2)
    # 风险控制原则
    select_option(0.866, 0.509, 0.866, 0.677)
    select_option(0.847, 0.588, 0.847, 0.701)
    select_option(0.854, 0.666, 0.831, 0.814)
    select_option(0.881, 0.751, 0.853, 0.881)
    # 点击提交
    mouse_click(0.891, 0.874)
    time.sleep(5)
    mouse_click(0.496, 0.792)
    time.sleep(5)
    much_mouse_click(0.678, 0.903, 2)
    time.sleep(30)


def profit_and_loss_measurement_module():
    """损益测算模块"""
    much_mouse_click(0.678, 0.903, 9, 3)
    time.sleep(5)
    # 调整概率
    pull_mouse(0.462, 0.348, 0.5, 0.34)
    pull_mouse(0.438, 0.418, 0.462, 0.424)
    mouse_click_and_input_content(0.497, 0.601, '21088.550')
    mouse_click_and_input_content(0.497, 0.65, '7039.944')
    mouse_click_and_input_content(0.497, 0.714, '18216.000')
    mouse_click(0.497, 0.788)
    time.sleep(5)
    mouse_click(0.500, 0.814)
    time.sleep(5)
    # 设定计算参数
    mouse_click(0.634, 0.364)
    mouse_click(0.634, 0.418)
    mouse_click_and_input_content(0.683, 0.527, '40')
    mouse_click_and_input_content(0.683, 0.590, '800')
    mouse_click_and_input_content(0.683, 0.648, '2540')
    mouse_click(0.498, 0.712)
    time.sleep(5)
    mouse_click(0.498, 0.7)
    time.sleep(5)
    # 计算变动成本
    pull_mouse(0.536, 0.453, 0.554, 0.453)
    mouse_click_and_input_content(0.502, 0.609, '2000')
    mouse_click(0.505, 0.709)
    time.sleep(5)
    mouse_click(0.505, 0.709)
    # 产品损益表
    mouse_click_and_input_content(0.552, 0.496, '16548.550')
    mouse_click_and_input_content(0.552, 0.540, '2499.944')
    mouse_click_and_input_content(0.552, 0.581, '13676.000')
    mouse_click(0.498, 0.672)
    time.sleep(2)
    mouse_click(0.745, 0.855)
    mouse_click(0.824, 0.833)
    much_mouse_click(0.678, 0.903, 3, 2)
    time.sleep(2)
    much_mouse_click(0.678, 0.903, 2, 2)
    # 点击记录
    time.sleep(6)
    mouse_click(0.608, 0.477)


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


# time.sleep(30)
# logger.info("前期配置开始")
# basis()
#
# logger.info("资源配置开始")
# resource_configuration_module()
#
# logger.info("商业配置开始")
# business_design_module()
#
# logger.info("市场配置开始")
# marketing_module()
#
# logger.info("利润损失配置开始")
# profit_and_loss_measurement_module()
#
#
# time.sleep(30)
# winsound.Beep(300, 1000)
# input("准备开始提交流程: ")
# submit_file_firefox_in_shiyanshi()
#
#
# time.sleep(10000)







