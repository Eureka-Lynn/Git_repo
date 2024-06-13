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
        all_data.append({
            "abstract": abstract,
            "title": title,
            "time": y+'-'+md.split('.')[0]
        })

# 根据页数爬取数据
for i in range(1, 126):
    r = requests.get('https://www.tjufe.edu.cn/tcxw/{}.htm'.format(i))
    r.encoding = 'utf-8'
    get_data(r)
r = requests.get('https://www.tjufe.edu.cn/tcxw.htm')
r.encoding = 'utf-8'
get_data(r)

# 将数据转换为json
json.dump(all_data, open('1.json', 'w',encoding='utf-8'), indent=4,ensure_ascii=False)

print('over')