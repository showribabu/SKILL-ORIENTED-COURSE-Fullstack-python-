from flask import Flask
#object to Flask
api=Flask(__name__)

#request handler
@api.route('/')
def homePage():
    return 'SIDDHARDHA1'

#server start

if __name__=="__main__":
    api.run(debug=True)

