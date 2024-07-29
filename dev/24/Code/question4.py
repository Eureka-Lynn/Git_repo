import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, classification_report
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor
from sklearn.ensemble import VotingRegressor

# 读取数据
with open ('D:/PY/dev/24/B/train.csv',encoding='utf-8') as f:
    data = pd.read_csv(f)
    data = data.drop(['id'],axis=1)

X = data.drop(['洪水概率'],axis=1)
y = data['洪水概率']

scaler = StandardScaler()
# 划分训练集与测试集
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)

# # 训练随机森林
# rf = RandomForestRegressor(n_estimators=100,random_state=42)
# rf.fit(X_train_scaled,y_train)

# # 模型正确性评估

# # 训练集预测洪水概率
# y_val_pred = rf.predict(X_val_scaled)

# # 计算评估指标
# mse = mean_squared_error(y_val, y_val_pred)
# r2 = r2_score(y_val, y_val_pred)
# print(mse,r2)
# 存储数据
# result_metrics = pd.DataFrame({
#     'Metric': ['Mean Squared Error', 'R^2 Score'],
#     'Value': [mse, r2]
# })
# result_metrics.to_csv('metrics.csv', index=False)
# print('over')

# # 训练逻辑回归模型
# log_reg = LinearRegression()
# log_reg.fit(X_train_scaled,y_train)

# # 评估模型
# y_val_pred = log_reg.predict(X_val_scaled)
# mse = mean_squared_error(y_val, y_val_pred)
# r2 = r2_score(y_val, y_val_pred)
# print(mse,r2)
# result_metrics = pd.DataFrame({
#     'Metric': ['Mean Squared Error', 'R^2 Score'],
#     'Value': [mse, r2]
# })
# result_metrics.to_csv('line_reg_metrics.csv', index=False)
# print('over')

# # XGboost训练
# xg = XGBRegressor(n_estimators = 100,learning_rate = 0.1,max_depth = 6)
# xg.fit(X_train_scaled,y_train)
# 概率预测
# y_val_pred = xg.predict(X_val_scaled)
# mse = mean_squared_error(y_val,y_val_pred)
# r2 = r2_score(y_val,y_val_pred)
# print(mse,r2)
# result_metrics = pd.DataFrame({
#     'Metric': ['Mean Squared Error', 'R^2 Score'],
#     'Value': [mse, r2]
# })
# result_metrics.to_csv('XGboost_metrics.csv', index=False)
# print('over')

# 使用堆叠法进行集成学习
# 基础模型类型
base_models = [
    ('rf', RandomForestRegressor(n_estimators=100)),
    ('lr', LinearRegression()),
    ('xgb', XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=6))
]
final_model = LinearRegression()
stacking_regressor = VotingRegressor(estimators=base_models)

# 训练
stacking_regressor.fit(X_train_scaled,y_train)
y_val_pred = stacking_regressor.predict(X_val_scaled)
mse = mean_squared_error(y_val,y_val_pred)
r2 = r2_score(y_val,y_val_pred)
print(mse,r2)
result_metrics = pd.DataFrame({
    'Metric': ['Mean Squared Error', 'R^2 Score'],
    'Value': [mse, r2]
})
result_metrics.to_csv('Stacking_Regressor_metrics.csv', index=False)
print('over')