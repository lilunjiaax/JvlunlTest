# Request URL: https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=40&format=json&keyword=%E8%A1%97%E6%8B%8D&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1561382214057

# 对于ajax爬虫其中的一个解决办法是通过分析network来寻求特定的url规律
'''
遇到的问题记录：请求到的data为none,可以大概确定服务器识别出这是爬虫
尝试添加一些headers头部信息来掩饰自己
比如：最基本的有referer,user-agent
还不行，尝试添加cookie信息。
'''
import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq
import os
from hashlib import md5
import time

base_url = 'https://www.toutiao.com/api/search/content/?'
headers = {
	'cookie': 'tt_webid=6706083417547589127; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6706083417547589127; UM_distinctid=16b899b9dc11fa-0882addaea872b-e343166-144000-16b899b9dc2410; csrftoken=fc86670fc33f7baeeaafd0deec33d0cf; CNZZDATA1259612802=1672063355-1561377529-%7C1561425693; __tasessionId=7mbqqg6931561426522141; s_v_web_id=9c8a0036cbe5aa877773d03834101dc6',
	'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
	'x-requested-with': 'XMLHttpRequest'
}


def get_timestamp():
	a = time.time()  
	# 1561426764.3656483
	# 1561426665 215
	b = str(a).split('.')
	return b[0]+b[1][0:3]


def get_page(offset,timestamp):
	params = {
		'aid': '24',
		'app_name': 'web_search',
		'offset': offset,
		'format': 'json',
		'keyword': '街拍',
		'autoload': 'true',
		'count': '20',
		'en_qc': '1',
		'cur_tab': '1',
		'from': 'search_tab',
		'pd': 'synthesis',
		'timestamp': timestamp
	}
	url = base_url+urlencode(params)
	print("url:",url)
	try:
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			print('json',response.json())
			return response.json()
			
	except requests.ConnectionError as e:
		print(e)


def get_content(json):
	if json:
		items = json.get('data')
		for item in items:
			# 要有title属性才可选择
			title = item.get('title')
			if title == None:
				continue
			else:
				image_list = item.get('image_list')
				for image in image_list:
					yield{
						'title': title,
						'image': image.get('url')
					}


def save_image(item):
	# item 就是上述生成器产生的字典
	if not os.path.exists(item.get('title')):
		os.mkdir(item.get('title'))
		print('建立文件夹:',item.get('title'))

	# 图片的命名就是用对应的md5值
	try:
		response = requests.get(item.get('image'))
		if response.status_code == 200:
			file_path = '{0}/{1}.{2}'.format(item.get('title'),md5(response.content).hexdigest(), 'jpg')
			if not os.path.exists(file_path):
				with open(file_path, 'wb') as f:
					f.write(response.content)
			else:
				print('----------already-download-----------',file_path)
	except:
		pass


if __name__ == "__main__":
	json = get_page(20,get_timestamp())
	image_list = get_content(json)
	for item in image_list:
		save_image(item)











