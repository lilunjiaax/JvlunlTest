
from selenium import webdriver
import time
browser = webdriver.Chrome()

'''
browser.get('https://www.baidu.com')

input = browser.find_element_by_id('kw')
input.send_keys('iphone')
time.sleep(3)
input.clear()

input.send_keys('ipad')
# input.submit()  # 对搜索框中的信息进行提交

# 按钮对象
buttom = browser.find_element_by_id('su')
# 点击按钮
buttom.click()

browser.close()
'''

# 获取标签的属性，获取文本

url = 'https://www.taobao.com'

browser.get(url)

banner_list = browser.find_elements_by_css_selector('.btn-search.tb-bg')
print(banner_list)
print(len(banner_list))
for item in banner_list:
	print(item.get_attribute('class'))
	print(item.get_attribute('href'))
	print(item.text)
	print(item.location)
	print(item.tag_name)




# browser.get('https://www.baidu.com')

# # 新建一个选项卡
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.switch_to_window(browser.window_handles[1])
# browser.get('https://www.taobao.com')

# time.sleep(2)
# browser.switch_to_window(browser.window_handles[0])
# browser.get('https://python.org')











