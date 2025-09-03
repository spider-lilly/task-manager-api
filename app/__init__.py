from flask import Flask
from flask_mysqldb import MySQL
from os import environ
from dotenv import load_dotenv,dotenv_values
mysql = MySQL()
load_dotenv()
def create_app():
    app = Flask(__name__)

   
    app.config.from_object("app.config.settings")
    mysql.init_app(app)
    from app.controller.main import bp
    app.register_blueprint(bp)

    return app
