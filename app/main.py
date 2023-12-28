from flask import Blueprint
from . import db

main = Blueprint('main', __name__)

# Get All Users
@main.route('/')
def index():
    return {"message": "Hello world"}

# Get All Users
@main.route('/user/all')
def get_all_users():
    return 'get all users'

# Get Users By Id
@main.route('/user/userid=<string:userId>')
def get_user_by_id(userId):
    return 'get user'

# Get Users By Email
@main.route('/user/email=<string:email>')
def get_user_by_email(email):
    return 'get user'

# Create user
@main.route('/user/create')
def create_user():
    return 'create user'

# Update User
@main.route('/user/update')
def update_user():
    return 'update user'

# Delete User By Email
@main.route('/user/delete/userid=<string:email>')
def delete_by_email(email):
    return 'delete user by mail'

# Delete User By Id
@main.route('/user/delete/userid=<string:userId>')
def delete_by_id(userId):
    return 'delete user by id'