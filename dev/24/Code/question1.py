import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']

# 将数据导入pandas中
with open ('D:/PY/dev/24/B/train.csv',encoding='utf-8') as f:
    data = pd.read_csv(f,encoding='utf-8')
    data = data.drop(['id'],axis=1)
# 使用斯皮尔曼相关系数检验
Spearman_matrix = data.corr(method='spearman')
Spearman_flood_corr = Spearman_matrix['洪水概率'].sort_values(ascending=False)
print('Spearman')
print(Spearman_flood_corr)
print('------------------------------------')


# mask = np.triu(np.ones_like(Spearman_matrix,dtype=bool))
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False

# plt.figure(figsize=(15,10))
# sns.heatmap(Spearman_matrix,annot=True,cmap='coolwarm',center=0,mask=mask,vmin=-0.01,vmax=0)
# plt.title('Spearman Correlation Matrix')
# plt.savefig('Spearman.png')

# 使用皮尔逊相关系数检验
Pearson_martix = data.corr(method='pearson')
Pearson_flood_corr = Pearson_martix['洪水概率'].sort_values(ascending=False)
print('Pearson')
print(Pearson_flood_corr)
print('------------------------------------')
# plt.figure(figsize=(15,10))
# sns.heatmap(Pearson_martix,annot=True,cmap='coolwarm',center=0,mask=mask,vmin=-0.012,vmax=0)
# plt.title('Pearson Correlation Matrix')
# plt.savefig('Pearson.png')

# 使用肯德尔相关系数检验
Kendall_matrix = data.corr(method='kendall')
# mask = np.triu(np.ones_like(Kendall_matrix,dtype=bool))
Kendall_flood_corr = Kendall_matrix['洪水概率'].sort_values(ascending=False)
print('Kendall')
print(Kendall_flood_corr)
print('------------------------------------')
# plt.figure(figsize=(15,10))
# sns.heatmap(Kendall_matrix,annot=True,cmap='coolwarm',center=0,mask=mask,vmin=-0.014,vmax=0)
# plt.title('Kendall Correlation Matrix')
# plt.savefig('Kendall.png')