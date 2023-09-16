from flask import Flask
from flask_restful import Api ,Resource ,reqparse ,abort

app = Flask(__name__)
api = Api(app) 

user_put_ars = reqparse.RequestParser()

user_put_ars.add_argument('user_name', type = str , required=True ,  help="error user name required ")
user_put_ars.add_argument('user_age', type = int , required=True ,   help="error user_age required ")
user_put_ars.add_argument('user_gender', type = str , required=True , help="error user_gender required ")
user_put_ars.add_argument('user_city', type = str , required=True ,   help="error user_city required ")

user_dict = {}

# abort if user not listed in user
#adding delete api 


#@app.errorhandler(404)
def abort_if_user_not_listed(ID):
    if ID not in user_dict:
        abort(404,message="user not listed")

def abort_if_user_exist(ID):
    if ID in user_dict:
        abort(404,message="user already exist")

class user(Resource):
    def get(self ,ID):
        abort_if_user_not_listed(ID)
        return user_dict[ID]
    def put(self ,ID):
        abort_if_user_exist(ID)
        args = user_put_ars.parse_args()
        user_dict[ID] = args
        return user_dict[ID]
    
api.add_resource(user,'/user/<int:ID>')
if __name__ == '__main__':
    app.run(debug=True)
