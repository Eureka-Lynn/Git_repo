from datetime import datetime
from collections import Counter
import json
import matplotlib.pyplot as plt

# 统计每月发布新闻
with open ('dev/dev/data/1.json','r',encoding='utf-8') as f:
    # 做一个哈希来存储每月数据
    month = Counter()
    data = json.load(f)
for _ in data:
    time = _['time']
    each_month = datetime.strptime(time,'%Y-%m').month
    month[each_month] += 1
# 对Conter生成的keys排序
sorted_month = sorted(month.items(),key=lambda x:x[0])
Months = []
Num = []
for _ in sorted_month:
    Months.append(_[0])
    Num.append(_[1])

# 画图
plt.rcParams['font.family'] = 'FangSong'
fig,ax = plt.subplots()
ax.set_xlabel('月份',fontsize = 15)
ax.set_ylabel('发文量',fontsize = 15)
ax.set_title('每月发文量',fontsize = 30)
ax.plot(Months,Num)
plt.savefig('dev/dev/figure/每月发文量.png',dpi = 300)