import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import jieba
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# 加载数据
df_train = pd.read_csv('online_shopping_train.csv')
df_train['review'] = df_train['review'].fillna('')

df_test = pd.read_csv('online_shopping_test.csv')
df_test['review'] = df_test['review'].fillna('')

# 使用结巴分词对 'review' 列进行分词
df_train['review'] = df_train['review'].apply(lambda x: ' '.join(jieba.cut(x)))
df_test['review'] = df_test['review'].apply(lambda x: ' '.join(jieba.cut(x)))

# 情感分析函数：使用 VADER 来获取情感分数
def sentiment_analysis(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_score = analyzer.polarity_scores(text)
    return sentiment_score['compound']

# 计算情感得分并将其添加为特征
df_train['sentiment_score'] = df_train['review'].apply(sentiment_analysis)
df_test['sentiment_score'] = df_test['review'].apply(sentiment_analysis)

# 数据预处理：特征和目标变量
y_train = df_train.iloc[:, 1].values  # 第二列为标签列
target_train = df_train.iloc[:, 3].values  # 第四列为target列

# 使用 TfidfVectorizer 提取文本特征
vectorizer = TfidfVectorizer(
    max_features=1500,       # 增加特征的数量
    ngram_range=(1, 2),      # 考虑 unigram 和 bigram 组合
    max_df=0.95,             # 忽略出现频率高于95%的单词
    stop_words='english'     # 去除常见的停用词（如适用）
)
X_train_tfidf = vectorizer.fit_transform(df_train['review'])
X_test_tfidf = vectorizer.transform(df_test['review'])

# 将情感得分作为额外的特征
X_train = np.hstack([X_train_tfidf.toarray(), df_train['sentiment_score'].values.reshape(-1, 1)])
X_test = np.hstack([X_test_tfidf.toarray(), df_test['sentiment_score'].values.reshape(-1, 1)])

# 定义模型
models = {
    'XGBoost': xgb.XGBClassifier(
        objective='binary:logistic',
        eval_metric='logloss',
        max_depth=5,
        learning_rate=0.05,
        n_estimators=1000,
        subsample=0.8,
        colsample_bytree=0.8,
        min_child_weight=2,
        scale_pos_weight=1
    ),
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Random Forest': RandomForestClassifier(n_estimators=100),
    'SVM': SVC(kernel='linear')
}

# 使用交叉验证（如StratifiedKFold）来评测多个模型
kf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
model_accuracies = {model: [] for model in models}

for train_index, val_index in kf.split(X_train, y_train):
    X_train_fold, X_val_fold = X_train[train_index], X_train[val_index]
    y_train_fold, y_val_fold = y_train[train_index], y_train[val_index]
    
    # 对每个模型进行训练和评估
    for model_name, model in models.items():
        # 训练模型
        model.fit(X_train_fold, y_train_fold)
        
        # 预测验证集
        y_pred = model.predict(X_val_fold)
        
        # 计算准确率
        accuracy = accuracy_score(y_val_fold, y_pred)
        model_accuracies[model_name].append(accuracy)

# 输出每个模型的平均准确率
for model_name, accuracies in model_accuracies.items():
    print(f'{model_name} - Average Accuracy: {np.mean(accuracies)}')

# 选择表现最好的模型进行预测（以 XGBoost 为例）
best_model_name = max(model_accuracies, key=lambda model: np.mean(model_accuracies[model]))
best_model = models[best_model_name]

# 使用整个训练集训练最佳模型
best_model.fit(X_train, y_train)

# 在测试集上进行预测
y_pred_all = best_model.predict(X_test)

# 保存预测结果为 CSV 文件
result_df = pd.DataFrame({'predicted_label': y_pred_all})
result_df.to_csv('online_shopping_prediction.csv', index=False)

print("预测结果已保存为 online_shopping_prediction.csv")
