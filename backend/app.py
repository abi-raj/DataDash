from flask import Flask,request,jsonify
import pandas as pd
app = Flask(__name__)


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
        for cname in lis:
          result[cname]=ndf[cname].tolist()
        return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)