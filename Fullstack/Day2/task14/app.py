#here no need of html page;


from flask import Flask #render_template,session,request,redirect
import mysql.connector as mysql

#obj..

app=Flask(__name__)

#mydb..
mydb=mysql.connect(
    user='root',
    host='localhost',database='showri',password='kits'
)
#cursor..in mydb..

mycursor=mydb.cursor()

#handler...

@app.route('/data',methods=['get'])
def data():
    sql='select * from babu'
    mycursor.execute(sql)
    res=mycursor.fetchall()
    data=[]
    for i in res:
        print(i)
        data.append(i)
    return str(data)

#server..

if __name__=='__main__':
    app.run(debug=True)
