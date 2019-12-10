#coding:utf8
'''
微博爬取思路：微博的内容时ajax加载的，所以需要分析出
网页在进行ajax加载时请求的地址和url变化规律，然后获取相应，
提取内容即可。
'''
import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq


base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
	'Referer': 'https://m.weibo.cn/u/2830678474',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
	'X-Requested-With': 'XMLHttpRequest',
}

def get_page(page):
	params = {
		'type':'uid',
		'value': '2830678474',
		'containerid': '1076032830678474',
		'page':page
	}

	url = base_url+urlencode(params)

	try:
		reponse = requests.get(url, headers=headers)
		print(reponse.status_code)
		if reponse.status_code == 200:
			# print(reponse.json())
			return reponse.json()
	except requests.ConnectionError as e:
			print('error'+'-----------',e.args)


def get_content(json):
	if json:
		items = json.get('data').get('cards')
		for item in items:
			'''此处还需要改善，因为获取的微博文本还需要做一些清洗处理'''
			weibo = {}
			item = item.get('mblog')
			weibo['id'] = item.get('id')
			weibo['text'] = pq(item.get('text')).text()
			weibo['attitude_count'] = item.get('attitudes_count')
			weibo['comments_count'] = item.get('comments_count')
			weibo['reposts_count'] = item.get('reposts_count')
			yield weibo



if __name__ == "__main__":
	json = get_page(1)
	item_list = get_content(json)
	for i in item_list:
		print(i)
	













