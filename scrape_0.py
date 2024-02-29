import requests
from bs4 import BeautifulSoup
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0'
}
for page in range(0,249,25):
    response=requests.get(f'https://movie.douban.com/top250?start={page}&filter=',headers=headers).text
    soup=BeautifulSoup(response,'html.parser')
    all_title=soup.find_all('span',attrs={'class':'title'})
    for i in all_title:
        title_string = i.string
        if '/' not in title_string:
            print(title_string)