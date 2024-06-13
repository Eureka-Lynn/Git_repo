import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.tjufe.edu.cn/../info/1004/11348.htm')
r.encoding = 'utf-8'
r_soup = BeautifulSoup(r.text,'lxml')
print(r_soup)