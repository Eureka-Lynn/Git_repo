from collections import Counter
import json
import matplotlib.pyplot as plt

# 依旧使用Counter，方便统计
look_n = Counter()
contri = Counter()
with open('dev/dev/data/2.json','r',encoding='utf-8') as f:
    data = json.load(f)
for _ in data:
    # 切片，去除‘供稿单位’字样和后面的换行，因为存在联合供稿情况，所以要分割一下
    string = _['Contributor'][5:].rstrip('\r\n    ').split('、')
    for i in string:
        # 供稿单位存在为空情况，剔除掉
        if i != '':
            contri[i] += 1
            # 记录阅览量
            look_n [i] += int(_['look_num'])
        # 然后发现了不得了的东西。。。https://www.tjufe.edu.cn/info/1004/21978.htm，这里的供稿单位写成了 克思主义学院。。。。。
# 我选择取前十五的单位
all = contri.most_common(15)
name = []
num = []
for _ in all:
    name.append(_[0])
    num.append(_[1])
# 然后出饼图
plt.rcParams['font.family'] = 'FangSong'
plt.title('各单位供稿统计',fontsize = 20)
plt.pie(num,labels=name,autopct='%1.1f%%')
plt.savefig('dev/dev/figure/各单位供稿情况.png',dpi = 300)
plt.close()

# 搞平均
total = []
for _ in all:
    # 用一个dict存储每个供稿单位数据
    dict = {
        'Name':_[0],
        'Num':_[1],
        'Look_num':look_n.get(_[0])
    }
    total.append(dict)
# 计算平均值
name = []
ave = []
for _ in total:
    average = int(_['Look_num'] / _['Num'])
    name.append(_['Name'])
    ave.append(average)
# 这里对平均阅读量从高到低做了排序，虽然这个方法有点麻烦了，但是我感觉是最好想的。
total = list(zip(name,ave))
name = []
ave = []
total = sorted(total,key = lambda x:x[1],reverse=True)
for _ in total:
    name.append(_[0])
    ave.append(_[1])
# 画柱状图
plt.figure(figsize=(20,8))
plt.title('供稿单位平均阅读量',fontsize = 30)
plt.xticks(fontsize = 15,rotation = 15)
plt.ylabel('平均阅读量',fontsize = 20)
plt.bar(name,ave)
plt.savefig('dev/dev/figure/供稿单位平均阅读量.png',dpi = 300)