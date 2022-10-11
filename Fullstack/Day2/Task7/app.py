
from flask import Flask,request

#here render_template is not used because no need of html page

#obj...
app=Flask(__name__)

#handler
#here data is passed at command line at url..so no need of the ....>request.form....>use request.args.get('var')
@app.route('/getdata',methods=['get'])
def getdata():
    name=request.args.get('name')
    roll=request.args.get('roll')
    print(name,roll)
    return 'Data collected'

#server start..

if __name__=='__main__':
    app.run(debug=True)
