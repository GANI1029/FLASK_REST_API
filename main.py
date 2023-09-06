from flask import Flask
from flask_restful import Api ,Resource

app = Flask(__name__)

api = Api(app)

class helloworld(Resource):
    def get(self):
        return {'message':'Hello World get request'}
    def post(self):

        return {'message':'Hello World post request'}
    

api.add_resource(helloworld,'/helloworld')

if __name__ == '__main__':
    app.run(debug=True)
