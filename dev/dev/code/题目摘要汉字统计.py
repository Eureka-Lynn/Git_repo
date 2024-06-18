import json
import jieba
import matplotlib.pyplot as plt
from collections import Counter
# 暴力遍历字符串拿字频数据没啥用,我感觉搞个词频统计会好玩点
# 因为要做中文分词，所以搞个jieba库，简单好使
c = Counter()
string = ''
# 判断字符是否为中文，提高之后词频统计效率
def is_chinese(char):
    if '\u4e00' <= char <= '\u9fff':
        return True
    else:
        return False
# 提前剔除一些词，提高统计效率
auxiliary = ['的','和','在','与','了','日','为','年','月','副','并','对','是','会','对','由','等','以']

with open('dev/dev/data/1.json','r',encoding='utf-8') as f:
    data = json.load(f)
# 将所有文本放在同一变量中
for _ in data:
    string += _['title']
    string += _['abstract']
# 词频统计
word = jieba.cut(string,cut_all=False)
word_split = '/'.join(word)
word_split = word_split.split('/')
for _ in word_split:
    if is_chinese(_) and _ not in auxiliary:
        c[_] += 1
# 根据词频绘图
Word = []
Times = []
plt.rcParams['font.family'] = 'FangSong'
fig,ax = plt.subplots(figsize = (22,13))
ax.set_xlabel('汉字',fontsize = 30)
ax.set_ylabel('出现次数',fontsize = 30)
ax.set_title('高频词统计',fontsize = 50)
common = c.most_common(50)
for _ in common:
    Word.append(_[0])
    Times.append(_[1])
ax.plot(Word,Times)
plt.xticks(Word,rotation=60,fontsize = 17)
plt.yticks(fontsize = 25)
plt.savefig('dev/dev/figure/标题概述高频词统计.png',dpi = 600)