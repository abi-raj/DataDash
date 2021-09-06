import pandas as pd 
import numpy as np
def dtype(df,cols):
    types={}
    for col in cols:
        if df[col].dtype == np.object:
            types[col] = 'String'
        else:
            types[col] = 'Number'
    return types

df=pd.read_csv('csv-tables.csv')
ndf=df.fillna(0)
lis=[i for i in ndf.columns]
print(lis)
result={}
result['columns']=lis
for cn in ndf.columns:
    result[cn]=ndf[cn].tolist()
print(len(ndf))
print(len(ndf.columns))
print(ndf.size)