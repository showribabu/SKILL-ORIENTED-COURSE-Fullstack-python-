from flask import Flask,render_template,redirect,request
import mysql.connector as mysql

#obj
app=Flask(__name__)

#mydb
mydb=mysql.connect(
    host='localhost',
    user='root',database='showri',password='kits'
)
mycursor=mydb.cursor()

@app.route('/formpage')
def formpage():
    return render_template('form.html')
@app.route('/loginerror')
def loginerror():
    return render_template('loginerror.html')
@app.route('/loginsuccess')
def loginsuccess():
    return render_template('loginsuccess.html')
@app.route('/registererror')
def registererror():
    return render_template('registererror.html')

@app.route('/registersucess')
def registersucess():
    return render_template('registersuccess.html')

@app.route('/loginpage')
def loginpage():
    return render_template('login.html')

@app.route('/')
def navigation():
    return render_template('navigation.html')

@app.route('/form',methods=['post'])
def form():
    name=request.form['name']
    roll=request.form['roll']
    password=request.form['pas']
    sql='select * from student'
    mycursor.execute(sql)
    res=mycursor.fetchall()
    for i in res:
        print(i)
        if name==i[0]:
            return redirect('/registererror')
    sql='insert into student(name,roll,pass) values(%s,%s,%s)'
    values=(name,roll,password)
    mycursor.execute(sql,values)
    return redirect('/registersucess')
       

            

@app.route('/login',methods=['post'])
def login():
    
    roll=request.form['roll']
    password=request.form['pas']
    sql='select * from student'
    mycursor.execute(sql)
    res=mycursor.fetchall()
    data=[]
    flag=0
    for i in res:
        data.append(i)
        if   roll==i[1] and password==i[2]:
            flag=1
    if flag==1:
        return redirect('/loginsuccess')
    else:
        return redirect('/loginerror')
        

@app.route('/log')
def logpage():
    return render_template('log.html')

if __name__=='__main__':
    app.run(debug=True)







    