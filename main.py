import pandas as pd
from sklearn.model_selection import StratifiedKFold
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from nltk.corpus import stopwords

def remove_stopwords(text):
    if pd.isnull(text):
        return text  # 跳过空值
    words = text.split()  # 分词
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

df = pd.read_csv('D:/Code/数管-大数据智能分析理论与方法/数管-实验报告模版/ai_generated_text/ai_generated_text/train_data.csv')
df_cleaned = df.drop_duplicates(subset=['text'], keep='first')
X = df_cleaned['text'].apply(lambda x: re.sub(r'', '', x.replace('\n', ' ').replace('\r', ' ')).strip())
y = df_cleaned['generated']
vectorizer = TfidfVectorizer(max_features=100)
model = DecisionTreeClassifier(max_depth = 4)
X = vectorizer.fit_transform(X)
model.fit(X,y)
test_df = pd.read_csv('D:/Code/数管-大数据智能分析理论与方法/数管-实验报告模版/ai_generated_text/ai_generated_text/test_data.csv')
X_test = test_df['text'].apply(lambda x: re.sub(r'', '', x.replace('\n', ' ').replace('\r', ' ')).strip())
X_test = vectorizer.fit_transform(X_test)
y_pred = model.predict(X_test)

ans = pd.DataFrame()
ans['predicted_label'] = y_pred
ans.to_csv('ans2.csv',index=False)
print('done')