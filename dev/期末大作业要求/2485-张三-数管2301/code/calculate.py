import json
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import pyplot as plt

print(plt.style.available)
plt.style.use('seaborn-v0_8')

rcParams['font.family'] = 'Heiti TC'

all_list = json.load(open('1.json', 'r'))
count_file = {

}
for each in all_list:
    count_file.setdefault(each['time'], 0)
    count_file[each['time']] += 1

print(count_file)

fig = plt.figure(dpi=300)
ax = fig.subplots()
ax.plot(count_file.keys(), count_file.values())
ax.set_xlabel('年月')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
ax.set_ylabel('发文数量')
plt.title('历史发文量')
plt.savefig('1.png')