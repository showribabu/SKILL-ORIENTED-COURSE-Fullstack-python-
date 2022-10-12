from flask import Flask,render_template

#obj..

app=Flask(__name__)

@app.route('/')
def navigate():
    return render_template('navigation.html')

@app.route('/home')
def home():
    return render_template('one.html')

@app.route('/about')
def about():
    return render_template('two.html')


if __name__=='__main__':
    app.run(debug=True)

