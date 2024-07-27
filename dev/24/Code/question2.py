import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.ensemble import RandomForestClassifier

# 读取数据
with open ('D:/PY/dev/24/B/train.csv') as f:
    data = pd.read_csv(f)
    data = data.drop(['id'],axis=1)
# 提取洪水概率，使用KMeans聚类
flood_probability = data[['洪水概率']]
kmeans = KMeans(n_clusters=3,random_state=42)
data['风险类别'] = kmeans.fit_predict(flood_probability)
# 根据风险类别分组
grouped = data.groupby('风险类别').mean()
# 计算不同指标权重
correlation_with_risk = data.corr()['风险类别'].abs().sort_values(ascending=False)
selected_indicators = correlation_with_risk.index[2:]
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
# 训练逻辑回归模型并且验证
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled,y_train)
baseline_model = y_pred = model.predict(X_test_scaled)
# 随机森林模型
model2 = RandomForestClassifier(n_estimators=100,random_state=42)
model2.fit(X_train_scaled,y_train)
baseline_model2 = y_pred_2 = model2.predict(X_test_scaled)
# 逻辑回归模型正确性
print('逻辑回归')
print(classification_report(y_test, y_pred))
# 随机森林正确性
print('随机森林')
print(classification_report(y_test,y_pred_2))
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
        'mean_change_down': np.mean(pred_down != baseline_model2)
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