from flask import Flask
from flask_restful import Api ,Resource ,reqparse ,abort , fields , marshal_with_field,marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

class Userdetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), unique=False, nullable=False)
    user_age = db.Column(db.Integer, unique=False, nullable=False)
    user_gender = db.Column(db.String(10), unique=False, nullable=False)
    user_city = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return f"Userdetails(id={self.id}, user_name='{self.user_name}', user_age={self.user_age}, user_gender='{self.user_gender}', user_city='{self.user_city}', email='{self.email}', phone={self.phone})"

#db.create_all() # --- requires only once to create a data base no need to run create second time it over rides database 


user_put_ars = reqparse.RequestParser()

user_put_ars.add_argument('user_name', type = str , required=True ,  help="error user name required ")
user_put_ars.add_argument('user_age', type = int , required=True ,   help="error user_age required ")
user_put_ars.add_argument('user_gender', type = str , required=True , help="error user_gender required ")
user_put_ars.add_argument('user_city', type = str , required=True ,   help="error user_city required ")
user_put_ars.add_argument('email', type = str , required=True ,   help="error user  email required ")
user_put_ars.add_argument('phone', type = int , required=True ,   help="error user  phone required ")

# using to update user data 
user_update_ars = reqparse.RequestParser()
user_update_ars.add_argument('user_name', type = str , required=False ,  help="error user name required ")
user_update_ars.add_argument('user_age', type = int , required=False ,   help="error user_age required ")
user_update_ars.add_argument('user_gender', type = str , required=False , help="error user_gender required ")
user_update_ars.add_argument('user_city', type = str , required=False ,   help="error user_city required ")
user_update_ars.add_argument('email', type = str , required=False ,   help="error user  email required ")
user_update_ars.add_argument('phone', type = int , required=False ,   help="error user  phone required ")

user_fields = {
    'id' : fields.Integer ,
    'user_name': fields.String,
    'user_age' : fields.Integer,
    'user_gender' : fields.String,
    'user_city' : fields.String,
    'email' : fields.String,
    'phone' : fields.Integer }

class user(Resource):
    @marshal_with(user_fields)
    def get(self ,ID):
        result  = Userdetails.query.filter_by(id = ID).first()
        if not result:
            abort(403 , message = 'could not find User ID...')

        return result
    
    @marshal_with(user_fields)
    def put(self ,ID):
        args = user_put_ars.parse_args()
        result  = Userdetails.query.filter_by(id = ID).first()

        if result:
            abort(409 , message = 'User ID taken...Use Different ID...')

        user = Userdetails(id = ID ,
                            user_name =args['user_name'] ,
                            user_age =args['user_age'] ,
                            user_gender =args['user_gender'] ,
                            user_city =args['user_city'] ,
                            email =args['email'] ,
                            phone =args['phone']  )
        db.session.add(user)
        db.session.commit()
        return user
    
    @marshal_with(user_fields)
    def patch(self ,ID):
        args = user_update_ars.parse_args()
        result  = Userdetails.query.filter_by(id = ID).first()

        if not result:
            abort(404 , message = "User ID doesn't exist... please use valid user id to update user details ")

        # Define a list of argument names to consider for updating
        updateable_fields = ['user_name', 'user_age', 'user_gender', 'user_city', 'email', 'phone']

        # Iterate through the argument names and update the Userdetails object if the argument is provided
        for field_name in updateable_fields:
            if args[field_name] is not None:
                setattr(result, field_name, args[field_name])

        db.session.commit()
        return result
    
    def delete(self, ID):
        result = Userdetails.query.filter_by(id=ID).first()

        if not result:
            abort(404, message="User ID doesn't exist... please use a valid user ID to delete the user")

        # Delete the user from the database
        db.session.delete(result)
        db.session.commit()

        return {'message': 'User deleted successfully', 'user id' : ID , 'user name':result.user_name }, 200  # 204 means No Content



    
api.add_resource(user,'/user/<int:ID>')

if __name__ == '__main__':
    app.run(debug=True)
