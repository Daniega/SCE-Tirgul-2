from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from db_create import db_create

app = Flask(__name__)
app.config.from_object('test_config')
app.app_context().push()
test_db = SQLAlchemy(app)
db_create(test_db)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

