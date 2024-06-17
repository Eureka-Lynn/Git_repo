# 简单的死没什么好说的
import matplotlib.pyplot as plt
import json
from collections import Counter

weekdays_look = Counter()
weekdays = Counter()

with open('dev/dev/data/2.json','r',encoding='utf-8') as f:
    data = json.load(f)
for _ in data:
    weekday = _['weekday']
    weekdays[weekday] += 1
    weekdays_look[weekday] += int(_['look_num'])

total = []
for _ in list(zip(weekdays.keys(),weekdays.values(),weekdays_look.values())):
    ave = _[2] / _[1]
    ave_week_look = {
        'Weekday':_[0],
        'Average_Look_Num':ave,
    }
    total.append(ave_week_look)
# 排序
total = sorted(total,key=lambda x:x['Average_Look_Num'],reverse=True)
Weekdays = []
Ave = []
for _ in total:
    Weekdays.append(_['Weekday'])
    Ave.append(_['Average_Look_Num'])
# 画图
plt.rcParams['font.family'] = 'FangSong'
plt.title('周数与平均阅读量',fontsize =20)
plt.ylabel('平均阅读量',fontsize = 15)
plt.bar(Weekdays,Ave)
plt.savefig('dev/dev/figure/周数与平均阅读量.png',dpi = 300)
