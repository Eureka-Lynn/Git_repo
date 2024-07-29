import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, classification_report
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import VotingRegressor
from xgboost import XGBRegressor


# 读取数据
with open ('D:/PY/dev/24/B/train.csv',encoding='utf-8') as f:
    data = pd.read_csv(f)
    data = data.drop(['id'],axis=1)
with open('D:/PY/dev/24/B/test.csv') as f:
    test_data = pd.read_csv(f)
    test_data = test_data.drop(['id'],axis=1)
scaler = StandardScaler()
X = data.drop(['洪水概率'],axis=1)
y = data['洪水概率']
X_test = test_data.drop(['洪水概率'],axis=1)
X_train_scaled = scaler.fit_transform(X)
X_test_scaled = scaler.transform(X_test)
# 使用投票法进行集成学习

# 基础模型类型
base_models = [
    ('rf', RandomForestRegressor(n_estimators=100)),
    ('lr', LinearRegression()),
    ('xgb', XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=6))
]
final_model = LinearRegression()
stacking_regressor = VotingRegressor(estimators=base_models)

# 训练
stacking_regressor.fit(X_train_scaled,y)
stacking_regressor_predictions = stacking_regressor.predict(X_test_scaled)
stack = pd.DataFrame()
stack[1] = stacking_regressor_predictions
stack.to_csv('stack_pred.csv')
test_data['洪水概率'] = stacking_regressor_predictions
test_data.to_csv('new_test.csv')
print('Everything Done')

