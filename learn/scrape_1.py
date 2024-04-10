import requests
from bs4 import BeautifulSoup
response=requests.get('http://books.toscrape.com/').text
output=BeautifulSoup(response,'html.parser')
all_title=output.find_all('h3',)
for i in all_title:
    real_title=i.find_all('a')
    for x in real_title:
        print(x.string)