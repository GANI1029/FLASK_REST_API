from flask import Flask
from flask_restful import Api ,Resource ,reqparse

app = Flask(__name__)
api = Api(app) 

user_put_ars =reqparse.RequestParser()
user_put_ars.add_argument('user_name', type = str , required=True ,  help="error user name required ")
user_put_ars.add_argument('user_age', type = int , required=True ,   help="error user_age required ")
user_put_ars.add_argument('user_gender', type = str , required=True , help="error user_gender required ")
user_put_ars.add_argument('user_city', type = str , required=True ,   help="error user_city required ")

user_dict = {
    'tom': {'user_name': 'Tom', 'user_age': 18},
    'jerry': {'user_name': 'Jerry', 'user_age': 10},
    'gani': {'user_name': 'gani', 'user_age': 25},  
}   

class user(Resource):
    def get(self ,ID):
        return {'id': ID}
    def put(self ,ID):
        args = user_put_ars.parse_args()

        return {ID : args}
    
api.add_resource(user,'/user/<int:ID>')
if __name__ == '__main__':
    app.run(debug=True)
