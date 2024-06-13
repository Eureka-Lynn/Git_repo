import json
import requests
from bs4 import BeautifulSoup

# 针对两种链接做不同处理
def U_Link_Data(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    r_soup = BeautifulSoup(r.text,'html.parser')
    sub_title = r_soup.find('div',class_= 'sub_title')
    # 获取发布时间
    date = sub_title.find('span',class_= 'time').text
    # 获取点击量稍微麻烦一点，因为它是用一个脚本返回的熬，数据可以通过get另外一个url来获得，只需要更改clickid就行，所以这里获取clickid
    clickid = sub_title.find('script').text.split(',')[2][1:-1]
    # 网站有基本反爬熬，加个headers模拟用户访问
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    r1 = requests.get('https://www.tjufe.edu.cn/system/resource/code/news/click/dynclicks.jsp?clickid={}&owner=1810941972&clicktype=wbnews'.format(clickid),headers=headers)
    r1.encoding = 'utf-8'
    look_num_page = BeautifulSoup(r1.text,'lxml')
    look_num = look_num_page.find('body').text
    # 接下来拿供稿单位,这里很蠢，做网站的把供稿单位的标签也打了class = look_num,所以要find_all，然后拿第二个
    Contributor = sub_title.find_all('span',class_='look_num')[1].text
    # 然后发现居然有不存在供稿单位的情况。。。。比如https://www.tjufe.edu.cn/../info/1004/11335.htm
    # 接下来拿正文数据



def W_Link_Data(url):
    pass





with open ('dev/dev/1.json','r',encoding='utf-8') as f:
    data = json.load(f)
    for _ in data:
        # 这里又有一点，如果链接转发自微信，它的abstract长度是为1的（我估计是一个换行符),通过abstract的长度来判断链接指向哪也是可以的
        # 首先对url类型做判断，微信链接和站内链接分别两种情况处理
        match _['url_type']:
            case 'U_Link':
                title = _['title']
                U_Link_Data(_['url'])
            case 'W_Link':
                title = _['title']
                W_Link_Data(_['url'])