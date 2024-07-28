import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from collections import Counter
from sklearn.preprocessing import MinMaxScaler

# 读取数据
with open ('D:/PY/dev/24/B/train.csv') as f:
    data = pd.read_csv(f)
    data = data.drop(['id'],axis=1)
# 提取洪水概率，使用KMeans聚类
flood_probability = data[['洪水概率']]
kmeans = KMeans(n_clusters=3,random_state=42)
data['风险类别'] = kmeans.fit_predict(flood_probability)
counter = Counter()
for _ in zip(data['洪水概率'],data['风险类别']):
    counter[_[0]] += 1
# 寻找边界值
max_2 = max(data[data['风险类别'] == 2]['洪水概率'])
min_1 = min(data[data['风险类别'] == 1]['洪水概率'])
colors = []
low_risk = (0, max_2)
medium_risk = (max_2, min_1)
high_risk = (min_1, 1)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(40,10))
for prob in counter.keys():
    if prob <= max_2:
        colors.append('#516B91')
    elif max_2 < prob <= min_1:
        colors.append('#59C4E6')
    else:
        colors.append('#EDAFDA')

legend_elements = [
    Line2D([0], [0], color='#516B91', lw=4, label='低风险'),
    Line2D([0], [0], color='#59C4E6', lw=4, label='中风险'),
    Line2D([0], [0], color='#EDAFDA', lw=4, label='高风险')
]
plt.title('洪水概率与风险类别分布')
plt.legend(handles=legend_elements, loc='upper right')
plt.bar(counter.keys(),counter.values(),width=0.003,color = colors)
plt.show('img.png')

# 根据风险类别分组
grouped = data.groupby('风险类别').mean()
grouped = grouped.drop('洪水概率',axis=1)
# 计算不同指标权重
correlation_with_risk = data.corr()['风险类别'].abs().sort_values(ascending=False)
selected_indicators = correlation_with_risk.index[2:]
sns.set(style='whitegrid')
plt.rcParams['font.sans-serif'] = ['SimHei']
grouped.T.plot(kind='bar',figsize=(20,10),color = ['#516B91', '#59C4E6','#EDAFDA'])
plt.title('不同风险系数指标平均值')
plt.ylabel('平均值')
plt.xlabel('指标')
plt.xticks(rotation = 45)
plt.ylim(4,5.5)
plt.tight_layout()
plt.legend(title='风险类别',loc='upper right')
plt.show('不同风险系数指标平均值.png')

# 权重归一化
weights = correlation_with_risk[selected_indicators]
weights = weights / weights.sum()
# 准备训练集
X = data[selected_indicators]
y = data['风险类别']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# 标准化数据
scalar = StandardScaler()
X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.transform(X_test)

X_train_scaled = pd.DataFrame(X_train_scaled, columns=selected_indicators)
X_test_scaled = pd.DataFrame(X_test_scaled, columns=selected_indicators)
# 训练逻辑回归模型
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled,y_train)
baseline_model = y_pred = model.predict(X_test_scaled)
# 随机森林模型
model2 = RandomForestClassifier(n_estimators=100,random_state=42)
model2.fit(X_train_scaled,y_train)
baseline_model2 = y_pred_2 = model2.predict(X_test_scaled)
# 逻辑回归模型正确性
model_report = classification_report(y_test,y_pred,output_dict=True)
model_report_pd = pd.DataFrame(model_report).transpose()
print('逻辑回归')
print(model_report)
# 随机森林正确性
model2_report = classification_report(y_test,y_pred_2,output_dict=True)
model2_report_pd = pd.DataFrame(model2_report).transpose()
print('随机森林')
print(model2_report)
# support归一化
scalar2 = MinMaxScaler()
model_report_pd['support'] = scalar2.fit_transform(model_report_pd['support'].values.reshape(-1,1))
model2_report_pd['support'] = scalar2.fit_transform(model2_report_pd['support'].values.reshape(-1,1))
# 存储数据
model_report_pd.to_csv('逻辑回归.csv')
model2_report_pd.to_csv('随机森林.csv')

# 可视化
def plot_classfication_report(report,title):
    plt.figure(figsize=(10,8))
    sns.heatmap(report,annot=True,cmap='coolwarm')
    plt.title(title)
    plt.savefig('{}.png'.format(title))
    plt.show()
plot_classfication_report(model_report_pd,'logic_regression')
plot_classfication_report(model2_report_pd,'random_forest')

# 灵敏度分析
def sensitivity_analysis(model, X_test_scaled, feature, delta=0.1):
    X_test_modified = X_test_scaled.copy()
    # 增加特征值
    X_test_modified[feature] = X_test_scaled[feature] * (1 + delta)
    pred_up = model.predict(X_test_modified)
    # 减少特征值
    X_test_modified[feature] = X_test_scaled[feature] * (1 - delta)
    pred_down = model.predict(X_test_modified)
    return pred_up, pred_down

sensitivity_results_log_reg = {}
sensitivity_results_rf = {}
for indicator in selected_indicators:
    # 逻辑回归模型
    pred_up, pred_down = sensitivity_analysis(model, X_test_scaled, indicator)
    sensitivity_results_log_reg[indicator] = {
        'mean_change_up': np.mean(pred_up != baseline_model),
        'mean_change_down': np.mean(pred_down != baseline_model)
    }
    # 随机森林模型
    pred_up, pred_down = sensitivity_analysis(model2, X_test_scaled, indicator)
    sensitivity_results_rf[indicator] = {
        'mean_change_up': np.mean(pred_up != baseline_model2),
        'mean_change_down': np.mean(pred_down != baseline_model2)
    }

# 转换为 DataFrame
sensitivity_df_log_reg = pd.DataFrame(sensitivity_results_log_reg).T
sensitivity_df_rf = pd.DataFrame(sensitivity_results_rf).T
# 输出灵敏度分析结果
print("逻辑回归模型的灵敏度分析结果：")
print(sensitivity_df_log_reg)
print("随机森林模型的灵敏度分析结果：")
print(sensitivity_df_rf)