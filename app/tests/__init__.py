from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import test_logic,test_web
from db_create import db_create

app = Flask(__name__)
app.config.from_object('flask_config')
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'



