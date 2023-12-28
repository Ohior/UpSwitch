from flask import Blueprint

Auth = Blueprint('Auth', __name__)

@Auth.route('/auth')
def default_route():
    return {"message":"Authorization"}


@Auth.route('/login')
def login():
    return 'Login'

@Auth.route('/signup')
def signup():
    return 'Signup'

@Auth.route('/logout')
def logout():
    return 'Logout'