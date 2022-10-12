from flask import Flask,render_template,request,session,redirect
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


#for store values....

@app.route('/message', methods=['post'])
def messageData():
    msg=request.form['message']
    session['msg']=msg
    #add data to session storage..
    print(session['msg'])
    #now after store store in session output redirect/navigate to output.html page
    return redirect('/output')

#data output to the output.html...so request handler for that also...
@app.route('/output')
def output():
    #return render_template('output.html') the var at output.html is msg...
    return render_template('output.html',m=session['msg'])


if __name__=='__main__':
    app.run(debug=True)

