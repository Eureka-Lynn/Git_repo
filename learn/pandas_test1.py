import pandas as pd

df= pd.read_csv('D:/PY/pandas/datas/beijing_tianqi/beijing_tianqi_2018.csv')

df.set_index('ymd',inplace=True)

df['bWendu']=df['bWendu'].str.replace('℃','').astype('int32')
df['yWendu']=df['yWendu'].str.replace('℃','').astype('int32')

print(df.dtypes)

print(df.head())