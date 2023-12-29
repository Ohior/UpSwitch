from apiflask import APIFlask

from services.main import Main
from services.auth import Auth

App = APIFlask(__name__)

App.register_blueprint(Main, url_prefix="/main")
App.register_blueprint(Auth, url_prefix="/auth")


@App.get("/")
def home():
    return {"message": "Hello world"}


if __name__ == '__main__':
    App.run(host='0.0.0.0', port=5000)
