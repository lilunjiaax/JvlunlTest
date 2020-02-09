
'''
流程梳理：
1.打开链家南京官网：https://nj.lianjia.com/
2.点击导航栏二手房的标签：
3.依次点击筛选条件：checked,雨花台区，获取到目标url
4.然后请求目标url来爬取完成3个页面任务(需要确定翻页策略)
翻页策略：
直接点击下一页来翻页
'''

import time
from selenium import webdriver
from urllib.parse import quote
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq 



browser = webdriver.Chrome()

base_url = 'https://nj.lianjia.com/'
wait = WebDriverWait(browser,10)
des_url = None

kind_house = '二手房'


def culti_url():
	# 根据筛选条件产生目标url
	
	browser.get(base_url)
	submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.nav.typeUserInfo > ul > li > a')))
	submit.click()

	# 选用xpath来选取雨花台标签











culti_url()

























# def list_page(page):
# 	"""
# 	:params page:页码
# 	"""
# 	print('正在爬取第 {} 页'.format(page))
# 	try:
# 		browser.get(url)
# 		# if page > 1:
# 		# 	# 进行跳转页面，然后再爬取
# 		# 	input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.form > input')))
# 		# 	submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.form > span.btn.J_Submit')))
# 		# 	print('------------------',submit.text)
# 		# 	input.clear()
# 		# 	input.send_keys(page)
# 		# 	submit.click()

# 		# 进行爬取
# 		# 某个节点文本中是否包含某文字(来以此判断页面是否加载完成)
# 		wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'li.item.active > span'), str(page)))
# 		wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.grid.g-clearfix')))
# 		get_product()
# 	except TimeoutException:
# 		list_page(page)




# def get_product():
# 	# 对于每一个浏览器正在显示的页面，进行页面解析
# 	html = browser.page_source
# 	doc = pq(html)
# 	items = doc('.item.J_MouserOnverReq').items()
# 	for item in items:
# 		print(item.find('.price').text())
# 		print(item.find('.deal-cnt').text())



# if __name__ == "__main__":
# 	list_page(2)
















