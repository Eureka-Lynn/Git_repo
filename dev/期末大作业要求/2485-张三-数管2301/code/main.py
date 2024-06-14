import requests
from bs4 import BeautifulSoup
import csv

all_list = []
for i in range(1, 100):
    r = requests.get('https://www.tjufe.edu.cn/tcxw/{}.htm'.format(i))
    r.encoding='utf-8'
    r_soup = BeautifulSoup(r.text, 'lxml')
    news_list_div = r_soup.find('ul', class_='news1_list')
    for each in news_list_div.find_all('li'):
        abstract = each.find('div', class_='text_con').text
        title = each.find('h6', class_='title').text
        time_div = each.find('div', class_='time')
        md = time_div.find('i').text
        y = time_div.find('span').text
        all_list.append({
            "abstract": abstract,
            "title": title,
            "time": y+'-'+md.split('.')[0]
        })
import json

json.dump(all_list, open('1.json', 'w',encoding='utf-8'), indent=4)
# wf = csv.DictWriter(open('1.csv', 'w', encoding='utf-8'), ['title', 'abstract', 'time'])
# wf.writeheader()
# wf.writerows(all_list)