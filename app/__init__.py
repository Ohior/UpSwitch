from apiflask import APIFlask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = APIFlask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlitedb.db'

    db.init_app(app)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
