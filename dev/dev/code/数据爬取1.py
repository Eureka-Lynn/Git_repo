import json
from datetime import datetime
import requests
from bs4 import BeautifulSoup

All_Web_Data = []
# 针对两种链接做不同处理
# 这个是Web链接
def U_Link_Data(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    r_soup = BeautifulSoup(r.text,'lxml')
    sub_title = r_soup.find('div',class_= 'sub_title')
    # 获取发布时间
    time = sub_title.find('span',class_= 'time').text
    # 获取点击量稍微麻烦一点，因为它是用一个脚本返回的熬，数据可以通过get另外一个url来获得，只需要更改clickid就行，所以这里获取clickid
    clickid = sub_title.find('script').text.split(',')[2][1:-1]
    # 网站有简单反爬机制，加个headers模拟用户访问
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
    content = r_soup.find('div',class_= 'item_info').text
    # 正文字数
    content_len = len(content)
    # 图片数量
    img = r_soup.find_all('img',class_='img_vsb_content')
    img_num = len(img)
    # 格式化处理时间数据,返回周几信息
    time = datetime.strptime(time,'%Y-%m-%d')
    weekday = datetime.weekday(time)
    weekdays = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
    weekday = weekdays[weekday]
    # 然后需要的数据就差不多拿完了
    Web_Data = {
        'weekday':weekday,
        'look_num':look_num,
        'Contributor':Contributor,
        'content':content,
        'content_length':content_len,
        'img_num':img_num,
    }
    All_Web_Data.append(Web_Data)

# 微信链接
def W_Link_Data(url):
    # r = requests.get(url)
    # r.encoding = 'utf-8'
    # r_soup = BeautifulSoup(r.text,'lxml')
    # 微信链接能拿的数据有点少,先获取发布时间
    # time = r_soup.find('em',id='publish_time').text
    # 这里拿发布时间也比较麻烦，是前端通过一个js返回的，目的是根据时间显示是今天还是昨天发布那种，像上面那行一样直接爬会返回一个空值
    # 网页源代码的var ct后面会返回一个时间戳，记录了发布时间，可以通过获取那个时间戳来获得文章发布时间，但是麻烦死了，不搞了......
    # 所以微信发布的文章直接跳过。。。。
    pass

with open ('dev/dev/data/1.json','r',encoding='utf-8') as f:
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
# 获取数据用json保存
json.dump(All_Web_Data,open('dev/dev/data/2.json','w',encoding='utf-8'),indent=4,ensure_ascii=False)

# 爬数据时间要挺久的，运行完了输出个提示
print('Over')