import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder,MinMaxScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import xgboost as xgb

# 读取数据
data = pd.read_csv("D:/PY/违约贷款/违约贷款/train.csv")

data = data[data['loan_default'] != 'a']

X = data.drop(columns = ['customer_id','main_account_loan_no', 'disbursed_date','loan_default','outstanding_disburse_ratio','branch_id','area_id','employee_code_id','manufacturer_id','supplier_id'])
y = data['loan_default']

X_train = X.astype(np.float64)
y_train = y.astype(np.float64)


correlation_matrix = X.corr()

# 设置相关性阈值
threshold = 0.3

upper_triangle = correlation_matrix.where(np.triu(np.ones(correlation_matrix.shape), k=1).astype(bool))

# 获取相关性大于 threshold 的特征对
to_drop = [column for column in upper_triangle.columns if any(abs(upper_triangle[column]) > threshold)]

# 删除相关性高的特征
X_reduced = X.drop(columns=to_drop)

dtrain = xgb.DMatrix(X_reduced,label=y_train)

params = {
    'objective': 'binary:logistic',        # 二分类任务
    'eval_metric': 'logloss',              # 评估指标
    'max_depth': 100,                        # 树的最大深度
    'eta': 0.1,                            # 学习率
    'subsample': 0.8,                      # 子样本比例
    'colsample_bytree': 0.8,               # 每棵树使用的特征比例
    'tree_method': 'gpu_hist',             # 启用 GPU 加速的树方法
    'gpu_id': 0                            # 使用第一个 GPU（如果有多个 GPU，可以选择其他编号）
}

num_round = 100
bst = xgb.train(params,dtrain,num_round)
importances = bst.get_score(importance_type='weight')  # 'weight', 'gain', 'cover' 等

# 转换为 DataFrame 便于处理
importances_df = pd.DataFrame(list(importances.items()), columns=['Feature', 'Importance'])

# 按重要性排序
importances_df = importances_df.sort_values(by='Importance', ascending=False)

top_n_features = importances_df.head(10)['Feature'].values
X_train_selected = X_train[top_n_features]
dtrain_selected = xgb.DMatrix(X_train_selected, label=y_train)
bst_selected = xgb.train(params, dtrain_selected, num_round)


test_data = pd.read_csv('D:/PY/违约贷款/违约贷款/test.csv')
X_test = test_data[top_n_features]
dtest_selected = xgb.DMatrix(X_test)
predictions = bst_selected.predict(dtest_selected)
predictions_bin = [1 if x > 0.5 else 0 for x in predictions]

result = pd.DataFrame({'predicted_label':predictions_bin})
result.to_csv('prediction.csv',index=False)
print('done')
