
import time
from selenium import webdriver
from urllib.parse import quote
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq 
import lxml
from xml.dom.minidom import Document


browser = webdriver.Chrome()
url = 'https://nj.lianjia.com/ershoufang/yuhuatai/l2a2p4/'
wait = WebDriverWait(browser,10)
browser.get(url)
browser.maximize_window()
item_list = []


def get_info():
	# 每到一个新的页面，要先获取最后的页码(activate)
	page_buttom = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.page-box.house-lst-page-box > a.on')))
	num = int(page_buttom.text)
	print('正在获取第 {} 页'.format(page_buttom.text))
	html = browser.page_source
	doc = pq(html)
	items = doc('.clear.LOGCLICKDATA').items()
	for item in items:
		info = item.find('.houseInfo').text()
		totalPrice = item.find('.totalPrice').text()
		unitPrice = item.find('.unitPrice').text()
		print(item.find('.houseInfo').text())
		print(item.find('.totalPrice').text())
		print(item.find('.unitPrice').text())
		item_list.append([totalPrice[0:-1],[i for i in info.replace(' ','').split('|') if '平米' in i][0], unitPrice[2:]])
	turn_next()
	return num
	



def turn_next():
	a_tag = browser.find_elements_by_xpath('//a[@class="on"]/../a')
	print(len(a_tag))
	last_tag = a_tag[-1]
	print('正在进行click: {}'.format(last_tag.text))
	last_tag.click()
	# page = browser.find_element_by_partial_link_text(u'下一页')
	# print(page.text)
	# browser.execute_script("arguments[0].scrollIntoView(false);",page)
	# WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, u'下一页'))).click()


def write_xml(list):
        #创建dom文档
        doc = Document()

        # 创建根节点
        itemlist = doc.createElement('itemlist')
        doc.appendChild(itemlist)

        for a_item in list:
            # 创建一个item结点，并插入到根节点上

            item = doc.createElement('item')
            itemlist.appendChild(item)

            #totalPrice结点
            link = doc.createElement('zongjia')
            link_text = doc.createTextNode(a_item[0])
            link.appendChild(link_text)
            item.appendChild(link)

            #mianji结点
            title = doc.createElement('mianji')
            title_text = doc.createTextNode(a_item[1])
            title.appendChild(title_text)
            item.appendChild(title)

            #unitPric结点
            doctor = doc.createElement('danjia')
            doctor_text = doc.createTextNode(a_item[2])
            doctor.appendChild(doctor_text)
            item.appendChild(doctor)

         

        with open('lianjia','wb+') as f:
            f.write(doc.toprettyxml(indent='\t',encoding='utf-8'))
        return



if __name__ == "__main__":
	while True:
		num = get_info()
		if num == 3:
			break
	write_xml(item_list)
















