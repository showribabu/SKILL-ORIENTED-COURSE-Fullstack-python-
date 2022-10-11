from flask import Flask,render_template,request

#obj..

app=Flask(__name__)

#handlers for both form and for to collects it data

#1..form render..
@app.route('/form')
def form():
    return render_template('form.html')

#2 form collects.. from form action name

@app.route('/data' ,methods=['post'])
def data():
    name=request.form['name']
    roll=request.form['roll']
    print(name,roll)
    return ('Data collected')


if __name__=='__main__':
    app.run(debug=True)
