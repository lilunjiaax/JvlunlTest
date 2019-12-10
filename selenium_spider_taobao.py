# coding:utf8
'''
淘宝的商品加载也是通过Ajax加载的，但是请求的url有一些加密，难以获得器规律
因此最好的就是采用selenium进行爬取，
采用selenium的好处，只要浏览器上能看到的，我就都可以爬取到。
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

kwords = '明基'
base_url = 'https://s.taobao.com/search?q='
wait = WebDriverWait(browser,10)
url = base_url + quote(kwords)



def list_page(page):
	"""
	:params page:页码
	"""
	print('正在爬取第 {} 页'.format(page))
	try:
		browser.get(url)
		if page > 1:
			# 进行跳转页面，然后再爬取
			input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.form > input')))
			submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.form > span.btn.J_Submit')))
			print('------------------',submit.text)
			input.clear()
			input.send_keys(page)
			submit.click()

		# 进行爬取
		# 某个节点文本中是否包含某文字
		wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'li.item.active > span'), str(page)))
		wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.grid.g-clearfix')))
		get_product()
	except TimeoutException:
		list_page(page)




def get_product():
	# 对于每一个浏览器正在显示的页面，进行页面解析
	html = browser.page_source
	doc = pq(html)
	items = doc('.item.J_MouserOnverReq').items()
	for item in items:
		print(item.find('.price').text())
		print(item.find('.deal-cnt').text())



if __name__ == "__main__":
	list_page(2)
	browser.close()





