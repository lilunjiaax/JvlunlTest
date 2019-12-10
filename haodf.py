import requests
from bs4 import BeautifulSoup
import re
import random
import  time
from xml.dom.minidom import Document
import heartrate
heartrate.trace(browser=True)
class Spider():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }
    def __spider(self):
        list = []
        for i in range(1, 35):
            link = 'https://zixun.haodf.com/dispatched/all.htm?p=' + str(i)
            response = requests.get(link, headers=self.headers, verify=False, timeout=10)
            # 每爬一个页面设置 休眠时间，若不设置会导致很多403
            time.sleep(random.randint(0, 3))
            print(str(i), 'status_code:', response.status_code)
            html_text = response.text
            soup = BeautifulSoup(html_text, 'lxml')
            item = soup.select('ul > li[class="clearfix"] > span')
            for count in range(0, 60, 2):
                list_temp = []
                try:
                    item_user = str(item[count]).split('a>')[1]
                    link = re.findall(r'href="(.*?)"', item_user)  # 帖子链接
                    title = re.findall(r'<a .*?>(.*?)</', str(item_user), re.S)  # 帖子标题
                    doctor_link_page = re.findall(r'href="(.*?)"', str(item[count + 1]))
                    doctor_name = re.findall(r'<a .*?>(.*?)</a>', str(item[count + 1]))
                    list_temp = [link[0], title[0], doctor_name[0], doctor_link_page[0]]
                    list.append(list_temp)
                except:
                    continue
        return list
    def __write_xml(self,list):
        #创建dom文档
        doc = Document()

        # 创建根节点
        orderlist = doc.createElement('orderlist')
        doc.appendChild(orderlist)

        for item in list:
            # 创建一个order结点，并插入到根节点上

            order = doc.createElement('order')
            orderlist.appendChild(order)

            #link结点
            link = doc.createElement('link')
            link_text = doc.createTextNode(item[0])
            link.appendChild(link_text)
            order.appendChild(link)

            #title结点
            title = doc.createElement('title')
            title_text = doc.createTextNode(item[1])
            title.appendChild(title_text)
            order.appendChild(title)

            #doctor结点
            doctor = doc.createElement('doctor')
            doctor_text = doc.createTextNode(item[2])
            doctor.appendChild(doctor_text)
            order.appendChild(doctor)

            #doctor_page结点
            doctor_link_page = doc.createElement('doctor_link_page')
            doctor_link_page_text = doc.createTextNode(item[3])
            doctor_link_page.appendChild(doctor_link_page_text)
            order.appendChild(doctor_link_page)

        with open('lsm','wb+') as f:
            f.write(doc.toprettyxml(indent='\t',encoding='utf-8'))
        return

    def go(self):
        list = self.__spider()
        self.__write_xml(list)


# 实现爬虫的断点重连
def retry_spider(func, sleep_time, retry_time):
    """
    func:实现爬虫的函数
    sleep_time:当程序报错后的休眠时间
    retry_time:最多尝试的次数
    """
    for i in range(retry_time):
        try:
            return func()
        except Exception as e:
            print('{0}:访问出错，{1}秒后重新启动，错误信息{2}'.format(__name__, sleep_time, e))
            time.sleep(sleep_time)
    print('{} 多次执行，均无法获得结果，请检查'.format(__name__))




def main():
    # 实例化爬虫类，spider.go()此函数是爬虫的入口
    spider = Spider()
    # 读取我设置的sleep_time , retry_time的参数
    try:
        sleep_time = int(sys.argv[1])
        retry_time = int(sys.argv[2])
    except:
        sleep_time = 5
        retry_time = 5
    try:
        spider.go()
    except:
        retry_spider(spider.go, sleep_time, retry_time)


if __name__ == "__main__":
    main()










