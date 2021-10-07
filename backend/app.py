from flask import Flask,request,jsonify
import pandas as pd
from flask_cors import CORS
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

app = Flask(__name__)
CORS(app)



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

@app.route('/pred',methods=['POST'])
def pred():
  data=request.get_json()
  
  # x=[1,2,3,4,5,6,7]
  # y=[2,3,4,5,6,7,8]
  x=data["x"]
  # print(x)
  y=data["y"]
  target=data["target"]
  xx=np.array(x).reshape((-1,1))
  yy=np.array(y).reshape((-1,1))
  # print(target)
  regr = LinearRegression()
  regr.fit(xx,yy)
  y_pred=regr.predict([[target]])
  return jsonify({"result":y_pred[0][0]})

if __name__ == '__main__':
    app.run(debug=True)