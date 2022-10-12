
from flask import Flask,render_template,request
import mysql.connector as mysql

#here data pass to  sql..
#so we need root,password,database,table,...
mydb= mysql.connect(
     host="localhost",
    user="root",
    password="kits",
    database="showri")

#cursor

mycursor=mydb.cursor()

   


#obj
app=Flask(__name__)

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/data',methods=['post'])
def data():
    name=request.form['name']
    roll=request.form['roll']
    print(name,roll)
    #......
    sql="INSERT INTO babu(name,roll)VALUES(%s,%s)"
    #....
    values=(name,roll)
    mycursor.execute(sql,values)
    mydb.commit()
    return 'Data collected'

#server..

if __name__=='__main___':
    app.run(debug=True)