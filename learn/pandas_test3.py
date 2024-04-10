import pandas as pd

fpath=('D:/PY/pandas/datas/beijing_tianqi/beijing_tianqi_2018.csv')
df=pd.read_csv(fpath)

df.loc[:,'bWendu']=df['bWendu'].str.replace('℃','').astype('int32')
df.loc[:,'yWendu']=df['yWendu'].str.replace('℃','').astype('int32')

df['wencha_type']=''
df.loc[df['bWendu']-df['yWendu']>10,'wencha_type']='温差大'
df.loc[df['bWendu']-df['yWendu']<=10,'wencha_type']='温差小'

print(df['wencha_type'].value_counts())