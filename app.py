from flask import Flask
from flask_restful import Api ,Resource

app = Flask(__name__)

api = Api(app)

class helloworld(Resource):
    def get(self):
        return {'message':'Hello World get request'}
    def post(self):

        return {'message':'Hello World post request'}

user_dict ={'tom' :{  'user_name': 'tom',  'user_age': 18 },
            'jerry' : {  'user_name': 'jerry',  'user_age': 10 } 
             }
    
class user(Resource):
    def get(self ,name):
        print(name)
        return user_dict[name]

    
api.add_resource(helloworld,'/helloworld')

api.add_resource(user,'/user/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)


