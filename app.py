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
    def get(self ,name):

        return user_dict['gani']
    
user_dict = {
    'tom': {'user_name': 'Tom', 'user_age': 18},
    'jerry': {'user_name': 'Jerry', 'user_age': 10},
    'gani': {'user_name': 'gani', 'user_age': 25},  
}
    
api.add_resource(helloworld,'/helloworld')

api.add_resource(user,'/user/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)

