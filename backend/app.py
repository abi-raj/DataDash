from flask import Flask,request,jsonify
import pandas as pd
app = Flask(__name__)
import numpy as np

#functions
def dtype(df,cols):
  result=[]
  lis=[]
  strCols=[]
  numCols=[]
  for col in cols:
    #print(str(df[col].dtype))
    if ((df[col].dtype)==np.object):
      lis.append('String')
      strCols.append(col)
    else:
      lis.append('Number')
      numCols.append(col)
  result.append(lis)
  result.append(strCols)
  result.append(numCols)
  return result

@app.route('/')
def hello_world():
  return 'Hello, World!'
  
@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        print(type(f))
        df=pd.read_csv(f,encoding='utf8')
        ndf=df.dropna()
        lis=[l for l in ndf.columns]
        result={}
        result['columns']=lis
        result['dtypes']=dtype(ndf,lis)
        result['totalSize']=str(ndf.size)
        result['rowSize']=str(len(ndf))
        for cname in lis:
          result[cname]=ndf[cname].tolist()
        return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)