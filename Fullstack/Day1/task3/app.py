from flask import Flask,render_template

#obj..

app=Flask(__name__)
#reqest..Response...

@app.route('/')
def homePage():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)
