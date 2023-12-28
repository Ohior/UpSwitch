from flask import Blueprint, request
from database.database_manager import DatabaseManager

from database.user_database import Session
from models.user_model import UserModel


Main = Blueprint('Main', __name__)


# Get All Users
@Main.route('/main', methods=['GET'])
def default_route():
    return {"message": "Main"}


# Get All Users
@Main.route('/user/all')
def get_all_users():
    allUsers = DatabaseManager.getAllUsers()
    return allUsers


# Get Users By Id
@Main.route('/user/userid=<string:userId>')
def get_user_by_id(userId):
    user = DatabaseManager.getUserByUserId(userId=userId)
    return user


# Get Users By Email
@Main.route('/user/email=<string:email>')
def get_user_by_email(email):
    user = DatabaseManager.getUserByEmail(email=email)
    return user


# Create user
@Main.route('/user/create', methods=["GET", "POST"])
def create_user():
    user = request.json
    print(user)
    user = DatabaseManager.createUser(userModel=UserModel(**request.json))
    return user


# Update User
@Main.route('/user/update')
def update_user():
    return 'update user'


# Delete User By Email
@Main.route('/user/delete/userid=<string:email>')
def delete_by_email(email):
    return 'delete user by mail'


# Delete User By Id
@Main.route('/user/delete/userid=<string:userId>')
def delete_by_id(userId):
    return 'delete user by id'
