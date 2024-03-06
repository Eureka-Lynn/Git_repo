import pandas as pd


fpath=('Tai1.csv')

df=(pd.read_csv(fpath))


# 时长转换为分钟
df.loc[:,'time']=df['时长']/60

print(df.describe())
print('==========================================')
print(df[df['time']>=30])
print('==========================================')
print(df.loc[df['time']>=30,:])