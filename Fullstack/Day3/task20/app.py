from flask import Flask,render_template,request
from pymongo import MongoClient

skills=[]

#obj..
app=Flask(__name__)

#monoclient..
client=MongoClient('localhost',27017)
#db...>database
db=client['showri']
#dbtabase-->collection..>tables...
coll=db['babu']






@app.route('/')
def form():
    return render_template('index.html')

@app.route('/form' ,methods=['post'])
def func():
    global skills
    print(request.form)
    name=request.form['name']
    roll=request.form['roll']
    if '1' in request.form:
        s1=request.form['1']
        skills.append(s1)
    if '2' in request.form:
        s2=request.form['2']
        skills.append(s2)
    if '3' in request.form:
        s3=request.form['3']
        skills.append(s3)
    print(name,roll,skills)
    k={}
    
    k['name']=name
    k['roll']=roll
    k['skills']=skills
    coll.insert_one(k)
    return 'data collected'

if __name__=='__main__':
    app.run(debug=True)

   
