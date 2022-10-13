from flask import Flask,request
from pymongo import MongoClient
app=Flask(__name__)

client = MongoClient('localhost',27017)
db=client['showri']
coll=db['babu']


@app.route('/getdata',methods=['get'])
def mongoData():
    k=coll.find()
    data=[]
    for i in k:
        data.append(i)
    return str(data)

if __name__ == '__main__':
    app.run(debug=True)