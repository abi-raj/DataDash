import io
from flask import Flask,request
from io import StringIO
import csv
from flask.json import jsonify
from flask_cors import CORS, cross_origin
import pandas as pd
from OpenSSL import SSL

# context = SSL.Context(SSL.TLSv1_2_METHOD)
# context.use_certificate('server.crt')
# context.use_privatekey('server.key')
app = Flask(__name__)
CORS(app, resources={r'/*': {"origins": '*'}})

def conver_to_json(csv_input):
    data={}
    csv_list=list(csv_input);
    columns=csv_list[0]
    data['columns']=columns
    for i in range(0,len(columns)):
        c_list=[]
        for j in range(1,len(csv_list)):
            c_list.append(csv_list[j][i])
        data[columns[i]]=c_list
    #print(data)

    return jsonify(data)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/upload', methods=['POST'])
# @cross_origin()
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        # c=pd.read_csv(StringIO(f.read()))
        # print(c)
        # stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
        # csv_input = csv.reader(stream)
        # print(type(csv_input))
        df=pd.read_csv(f)
        print(df.shape)
    #print("file contents: ", file_contents)
    #print(type(file_contents))
        # print(csv_input)
        # for row in csv_input:
        #     print(row)
        # cs=pd.read_csv(f)
        # print(cs.to_json())
        #fstring=f.read()
        #print(fstring)
        # csv_dicts = [{k: v for k, v in row.items()} for row in csv.DictReader(fstring.splitlines(), skipinitialspace=True)]
        # print(csv_dicts)
        return df.shape

if __name__ == '__main__':
    app.run(debug=True)