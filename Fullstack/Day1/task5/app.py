from flask import Flask,render_template

#obj

server=Flask(__name__)

#handler
#for each html file we write handler

@server.route('/')
def index():
    return render_template('register.html')




#server runner..

if __name__=='__main__':
    server.run(debug=True)
