import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression


with open('D:/PY/dev/24/B/train.csv') as f:
    data = pd.read_csv(f)
    data = data.drop(['id'],axis=1)
indicators = ['季风强度','地形排水','河流管理','森林砍伐','城市化','气候变化','大坝质量','淤积','农业实践','侵蚀','无效防灾','排水系统','海岸脆弱性','滑坡','流域','基础设施恶化','人口得分','湿地损失','规划不足','政策因素']
target = '洪水概率'


x = data[indicators]
y = data[target]


# 标准化数据
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)
# 聚类分析
kmeans = KMeans(n_clusters=3,random_state=0)
data['风险类别'] = kmeans.fit_predict(x_scaled)
centers = scaler.inverse_transform(kmeans.cluster_centers_)
# 不同风险类别指标特征
risk_analysis = data.groupby('风险类别')[indicators].mean()
print(risk_analysis)
# 根据指标计算权重
model = LinearRegression()
model.fit(x,y)
weights = model.coef_
weights_df = pd.DataFrame(
    {'指标':indicators,
     '权重':weights,
    })
weights_dict = weights_df.set_index('指标')['权重'].to_dict()
# 通过加权平均建立预警评价模型
def risk_score(row,weights):
    return sum(row[ind] * weights.get(ind) for ind in weights.keys())
data['风险评分'] = data.apply(lambda row: risk_score(row, weights_dict), axis=1)
data['预警类别'] = pd.qcut(data['风险评分'], q=3, labels=['低风险', '中风险', '高风险'])
# 将数据导出，避免反复处理数据浪费时间
data.to_csv('question2_data.csv', index=False,encoding='utf-8')
print('over')