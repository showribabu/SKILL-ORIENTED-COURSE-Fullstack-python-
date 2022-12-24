from flask import Flask,redirect,render_template,request

#obj..
app=Flask(__name__)

#handlers..
@app.route('/')
def card():
    return render_template('card.html')

@app.route('/cdata',methods=['post'])
def cdata():
    name=request.form['name']
    clg=request.form['clg']
    pf=request.form['photo']
    return render_template('out.html' ,c=clg,n=name)


#server..
if __name__=='__main__':
    app.run(debug=True)