import matplotlib.pyplot as plt
import json
from collections import Counter

Contributor = Counter()
All_content = Counter()
All_img = Counter()
Ave = []

with open('dev/dev/data/2.json','r',encoding='utf-8') as f:
    data = json.load(f)
for _ in data:
    Contri = _['Contributor'][5:-6]
    content = _['content_length']
    img = _['img_num']
    Contributor[Contri] += 1
    All_content[Contri] += content
    All_img[Contri] += img
# 取发文数前十五，求各项平均
for _ in Contributor.most_common(15):
    Name = _[0]
    Ave_Content = All_content.get(Name) / _[1]
    Ave_Img = All_img.get(Name) / _[1]
    dict = {
        'Name':Name,
        'Ave_Content':Ave_Content,
        'Ave_Img':Ave_Img
    }
    Ave.append(dict)
# 画
plt.figure(figsize=(16,8))
plt.rcParams['font.family'] = 'FangSong'
for _ in Ave:
    name = _['Name']
    x = _['Ave_Content']
    y = _['Ave_Img']
    plt.scatter(x,y,label = name,s = 80)
    # 把点放大不然我要瞎了
plt.title('各供稿单位平均字数与图片数',fontsize = 30)
plt.xlabel('平均字数',fontsize = 20)
plt.ylabel('平均图片数',fontsize = 20)
plt.minorticks_on()
plt.legend(loc = 2)
plt.savefig('dev/dev/figure/各供稿单位平均字数与图片数.png',dpi = 300)