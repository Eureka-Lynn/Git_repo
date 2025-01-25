import pandas as pd
from sklearn.model_selection import StratifiedKFold
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
def remove_stopwords(text):
    if pd.isnull(text):
        return text  # 跳过空值
    words = text.split()  # 分词
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)

df = pd.read_csv('D:/Code/数管-大数据智能分析理论与方法/数管-实验报告模版/ai_generated_text/ai_generated_text/train_data.csv')
df_cleaned = df.drop_duplicates(subset=['text'], keep='first')
# 去重，describe发现存在重复行
X = df_cleaned['text'].apply(lambda x: re.sub(r'', '', x.replace('\n', ' ').replace('\r', ' ')).strip())
X = X.apply(remove_stopwords)
y = df_cleaned['generated']
vectorizer = TfidfVectorizer(max_features=100)
rf_model = RandomForestClassifier(n_estimators=100,n_jobs=-1)
X = vectorizer.fit_transform(X)
feature_names = vectorizer.get_feature_names_out()
print(feature_names)
rf_model.fit(X,y)
test_df = pd.read_csv('D:/Code/数管-大数据智能分析理论与方法/数管-实验报告模版/ai_generated_text/ai_generated_text/test_data.csv')
X_test = test_df['text'].apply(lambda x: re.sub(r'', '', x.replace('\n', ' ').replace('\r', ' ')).strip())
X_test = vectorizer.fit_transform(X_test)
y_pred = rf_model.predict(X_test)



ans = pd.DataFrame()
ans['predicted_label'] = y_pred
ans.to_csv('ans.csv',index=False)
print('done')