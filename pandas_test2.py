import pandas as pd

df=pd.read_csv('D:/PY/Tai1.csv')

df.set_index('时间',inplace=True)

print(df.loc['01/01/2024 00:00:00','标题'])