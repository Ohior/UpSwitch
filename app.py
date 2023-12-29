from apiflask import APIFlask

from services.main import Main
from services.auth import Auth

App = APIFlask(__name__)

App.register_blueprint(Main, url_prefix="/main")
App.register_blueprint(Auth, url_prefix="/auth")


@App.get("/")
def home():
    return {"message": "Hello world"}
