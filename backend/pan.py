import pandas as pd 


df=pd.read_csv('dataset.csv')
ndf=df.dropna()
lis=[i for i in ndf.columns]
print(lis)
result={}
result['columns']=lis
for cn in ndf.columns:
    result[cn]=ndf[cn].tolist()
print(result)