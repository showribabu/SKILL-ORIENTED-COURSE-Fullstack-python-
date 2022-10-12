from flask import Flask,render_template,request,session
#obj..
#for session storage import the session class also

app=Flask(__name__)

#secrect key to that message..

app.secret_key='Showri'
#secret ketynhas key:value...
#here key is our own and,....value from form

#handlere for html render & collect data from form

@app.route('/form')
def form():
    return render_template('index.html')

@app.route('/message', methods=['post'])
def messageData():
    msg=request.form['message']
    session['msg']=msg
    #add data to session storage..
    print(session['msg'])
    return 'Message stored'

if __name__=='__main__':
    app.run(debug=True)

