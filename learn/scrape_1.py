import requests
from bs4 import BeautifulSoup
while True:
    response=requests.get('http://211.81.31.19/').text