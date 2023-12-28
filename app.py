from apiflask import APIFlask

from services.main import Main
from services.auth import Auth


App = APIFlask(__name__)

App.register_blueprint(Main)
App.register_blueprint(Auth)


@App.get("/")
def home():
    return {"message": "Hello world"}
