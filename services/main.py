from flask import Blueprint, request

from database.database_manager import DatabaseManager
from models.user_model import UserModel

Main = Blueprint('Main', __name__)


@Main.route('/', methods=['GET'])
def default_route():
    return {"message": "Main"}


# Get All Users
@Main.route('/user/all', methods=["GET"])
def get_all_users():
    allUsers = DatabaseManager.getAllUsers()
    return allUsers


# Get Users By Id
@Main.route('/user/userid=<string:userId>', methods=["GET"])
def get_user_by_id(userId):
    user = DatabaseManager.getUserByUserId(userId=userId)
    return user


# Get Users By Email
@Main.route('/user/email=<string:email>', methods=["GET"])
def get_user_by_email(email):
    print(f"USER")
    user = DatabaseManager.getUserByEmail(email=email)
    print(f"USER {user}")
    return user


# Create user
@Main.route('/user/create', methods=["GET", "POST"])
def create_user():
    user = DatabaseManager.createUser(userModel=UserModel(**request.json))
    return user


# Update User
@Main.route('/user/update/userid=<string:userId>', methods=["GET", "PUT"])
def update_user_by_id(userId):
    user = DatabaseManager.updateUserById(userId, request.json)
    return user


@Main.route('/user/update/email=<string:email>', methods=["GET", "PUT"])
def update_user_by_email(email):
    user = DatabaseManager.updateUserByEmail(email, request.json)
    return user


# Delete User By Email
@Main.route('/user/delete/email=<string:email>', methods=["DELETE"])
def delete_by_email(email):
    user = DatabaseManager.deleteUserByEmail(email)
    return user


# Delete User By Id
@Main.route('/user/delete/userid=<string:userId>', methods=["DELETE"])
def delete_by_id(userId):
    user = DatabaseManager.deleteUserByUserId(userId)
    return user
