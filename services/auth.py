
from flask import Blueprint, request

from database.database_manager import DatabaseManager
from models.user_model import UserModel
from werkzeug.security import generate_password_hash

from utils.tools import Tools

Auth = Blueprint('Auth', __name__)


@Auth.route('/auth')
def default_route():
    return {"message": "Authorization"}


@Auth.route('/signup', methods=["POST"])
def signup():
    hashUser = request.json
    hashUser["password"] = generate_password_hash(str(hashUser['password']))
    user = DatabaseManager.signUpUser(
        UserModel(
            **hashUser,
            isAuth=True,
            userId=Tools.generateUUID()
        )
    )
    return user


@Auth.route('/login/userid=<string:userId>', methods=["GET", "PUT"])
def loginByUserId(userId):
    user = DatabaseManager.logInUserById(userId, request.json)
    return user


@Auth.route('/login/email=<string:email>', methods=["PUT"])
def loginByEmail(email):
    print(f"VALUES 1 {request.json}")
    user = DatabaseManager.logInUserByEmail(email, request.json)
    return user


@Auth.route('/logout/email=<string:email>', methods=["GET", "PUT"])
def logoutByEmail(email):
    user = DatabaseManager.logOutUserByEmail(email)
    return user


@Auth.route('/logout/userid=<string:userId>', methods=["GET", "PUT"])
def logoutByUserId(userId):
    user = DatabaseManager.logOutUserByUserId(userId)
    return user
