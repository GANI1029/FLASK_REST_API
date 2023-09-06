from flask import Flask
from flask_restful import Api ,Resource

app = Flask(__name__)

api = Api(app)

class helloworld(Resource):
    def get(self):
        return {'message':'Hello World get request'}
    def post(self):

        return {'message':'Hello World post request'}
    
class user(Resource):
    def get(self ,name,age):
        return {'user_name': name , 'user_age': age}
    def post(self):

        return {'message':'user post request'}
    
api.add_resource(helloworld,'/helloworld')

api.add_resource(user,'/user/<string:name>/<int:age>')

if __name__ == '__main__':
    app.run(debug=True)


