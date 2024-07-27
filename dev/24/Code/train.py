
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']

# 将数据导入pandas中
with open ('D:/PY/dev/24/B/data/train.csv') as f:
    data = pd.read_csv(f)
    data = data.drop(['id'],axis=1)
# 使用斯皮尔曼相关系数检验
Spearman_matrix = data.corr(method='spearman')
Spearman_flood_corr = Spearman_matrix['洪水概率'].sort_values(ascending=False)
print('Spearman')
print(Spearman_flood_corr[:10])
print('------------------------------------')
# plt.figure(figsize=(15,10))
# sns.heatmap(Spearman_matrix,annot=True,cmap='coolwarm',center=0)
# plt.title('Spearman Correlation Matrix')
# plt.show()

# 使用皮尔逊相关系数检验
Pearson_martix = data.corr(method='pearson')
Pearson_flood_corr = Pearson_martix['洪水概率'].sort_values(ascending=False)
print('Pearson')
print(Pearson_flood_corr[:10])
print('------------------------------------')
# plt.figure(figsize=(15,10))
# sns.heatmap(Pearson_martix,annot=True,cmap='coolwarm',center=0)
# plt.title('Pearson Correlation Matrix')
# plt.show()

# 使用肯德尔相关系数检验
# Kendall_matrix = data.corr(method='kendall')
# Kendall_flood_corr = Kendall_matrix['洪水概率'].sort_values(ascending=False)
# print('Kendall')
# print(Kendall_flood_corr)
# print('------------------------------------')
# plt.figure(figsize=(15,10))
# sns.heatmap(Kendall_matrix,annot=True,cmap='coolwarm',center=0)
# plt.title('Kendall Correlation Matrix')
# plt.show()