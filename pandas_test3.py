import pandas as pd

fpath=('D:/PY/pandas/datas/beijing_tianqi/beijing_tianqi_2018.csv')
df=pd.read_csv(fpath)

df.loc[:,'bWendu']=df['bWendu'].str.replace('℃','').astype('int32')
df.loc[:,'yWendu']=df['yWendu'].str.replace('℃','').astype('int32')

df.assign(
    yWendu_huashi = lambda x : x["yWendu"] * 9 / 5 + 32,
    # 摄氏度转华氏度
    bWendu_huashi = lambda x : x["bWendu"] * 9 / 5 + 32
)
