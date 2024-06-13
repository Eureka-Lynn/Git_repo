import requests
from bs4 import BeautifulSoup
import json

# 创建一个空列表用于存储网页数据
all_data = []

# 对爬取源数据做处理
def get_data(r):
    r_soup = BeautifulSoup(r.text, 'lxml')
    news_list_div = r_soup.find('ul', class_='news1_list')
    for each in news_list_div.find_all('li'):
        abstract = each.find('div', class_='text_con').text
        title = each.find('h6', class_='title').text
        time_div = each.find('div', class_='time')
        md = time_div.find('i').text
        y = time_div.find('span').text
        url = each.find('a').get('href')
        # 这里发现一点，并非所有url都为/info/1004/.....的格式，部分是直接转发微信链接
        # 对url做一个切片，若首字母为h则说明是转发微信链接
        if url[0] == 'h':
            link = url
            type = 'W_Link'
        else:
            link = 'https://www.tjufe.edu.cn/' + url
            type = 'U_Link'
        all_data.append({
            "abstract": abstract,
            "title": title,
            "time": y+'-'+md.split('.')[0],
            'url':link,
            'url_type':type
        })

# 按页数爬取数据
for i in range(1, 126):
    r = requests.get('https://www.tjufe.edu.cn/tcxw/{}.htm'.format(i))
    r.encoding = 'utf-8'
    get_data(r)
# 新闻首页没法用上面的方式访问，单独写一个
r = requests.get('https://www.tjufe.edu.cn/tcxw.htm')
r.encoding = 'utf-8'
get_data(r)

# 将数据转换为json并存储
json.dump(all_data, open('dev/dev/1.json', 'w',encoding='utf-8'), indent=4,ensure_ascii=False)

print('over')