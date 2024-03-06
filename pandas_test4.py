import pandas as pd


fpath=('Tai1.csv')

df=(pd.read_csv(fpath))

df.set_index('时间',inplace=True)

# 时长转换为分钟
df.loc[:,'time']=df['时长']/60
df[u'time']=df[u'time'].apply(lambda x : format (x,'.2'))
df['time']=df['time'].astype('float32')


print(df.loc[df['time']>=30,:])